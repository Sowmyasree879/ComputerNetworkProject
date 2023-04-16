import xml.etree.ElementTree as ET
import json
import socket
import os

while True:
    print("\n ----------------------------------\n")
    host = "127.0.0.1"
    check = {}
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # listen on localhost port 1337
    s.bind((host, 1337))
    # queue up to 5 requests
    s.listen(5)
    
    # establish a connection
    clientsocket, client_ip = s.accept()
    print("\n[+] received a data from -> {}".format(client_ip))
    # open a file with a random name and insert the decoded data into it
    while True:
        # get the encoded data
        encoded_data = clientsocket.recv(4096)
        if not encoded_data:
            clientsocket.close()
            break
        else:
            check = encoded_data.decode("utf-8")
            
    data = json.loads(check)

    with open(data["filename"], 'w') as f:
        for line in data["Lines"]:
            f.write(line)
    Values = list(data.values())
    tree = ET.parse(Values[0])
    root = tree.getroot()
    method = ''

    for item in root.findall('./method'):
        string = (item.text.encode("utf-8"))
        method = string.decode("utf-8")

    args = []
    result = []
    print("method requested = {}".format(method))
    print("server executing {}.py".format(method))
    if method == "reverse":
        for item in root.findall('./arg'):
            string = (item.text.encode("utf-8"))
            args.append(string.decode('utf-8'))

        services = os.popen('''python reverse.py {}'''.format(args[0]))
        print(services)
        for line in services:
            result.append(line)

    if method == "square":
        for item in root.findall('./arg'):
            string = (item.text.encode("utf-8"))
            args.append(string.decode('utf-8'))

        services = os.popen("python square.py {}".format(args[0]))
        for line in services:
            result.append(line)

    if method == "sum":
        for item in root.findall('./arg'):
            string = (item.text.encode("utf-8"))
            args.append(string.decode('utf-8'))

        new = ""
        for i in args:
            new = new + ' ' + i
        services = os.popen("python sum.py {}".format(new))
        for line in services:
            result.append(line)

    if method == "sort":
        for item in root.findall('./arg'):
            string = (item.text.encode("utf-8"))
            args.append(string.decode('utf-8'))

        new = ''
        for i in args:
            new = new + ' ' + str(i)

        services = os.popen("python sort.py {}".format(new))
        for line in services:
            result.append(line)

    if method == "equation":
        for item in root.findall('./arg'):
            string = (item.text.encode("utf-8"))
            args.append(string.decode('utf-8'))

        new = ''.join(args)

        services = os.popen('''python calc.py "{}"'''.format(new))
        for line in services:
            result.append(line)

    # --------------------------------------------------

    if method == "path":

        Result = {}

        # Iterate over each node element in the root
        for node in root.findall('node'):
            name = node.find('name').text
            args = [arg.text for arg in node.findall('arg')]
            Result.setdefault(name, args)

        start = root.find('start').text
        end = root.find('end').text

    
        services=os.popen('''python path.py "{}" "{}" "{}"'''.format(Result,start,end))
        for line in services:
            result.append(line)

    #----------------------------------------------------

    ans=result[0].replace('\n','')
    print("Result = {}".format(ans))
    print("Encoding Result in XML")
    print("sending result back to client")

    XML_="<envelope><method>result</method><arg>{}</arg></envelope>".format(ans)
    reply={"xml":XML_}
    encoded_data=json.dumps(reply)
    # send data to command and control server
    # create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to command and control server on port 1337
    s.connect(("127.0.0.1", 1447))
    s.send(bytes(encoded_data,encoding="utf-8"))
    s.close()