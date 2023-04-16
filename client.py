import xml.etree.ElementTree as ET  # Importing the ElementTree module from the xml package
import json  # Importing the json module
import socket  # Importing the socket module
import os  # Importing the os module

 
def ava_files():
    # This function execute at start of client code
	# This functon execute when user want to execute it own xml file
	# it shows list of all xml files 
	# user select a pre genrated xml file
    cwd = os.getcwd()  # Getting the current working directory
    print('\nSelect Filename From availaible Filenames:')
    print("------------------------------------------\n")

    # List all files in the current working directory
    files = os.listdir("{}".format(cwd))  # Retrieving a list of all filenames in the current directory using the os module

    for file in files: # loop of all files in filename
        print(file)  # Printing each filename in the list

    print("\n---------------------------------------------")
    filename = input("Filename: ")  # Prompting the user to enter a filename
    return filename  # Returning the user's selected filename as a string

def ava_methods():
	# Display available methods
	print("select your method from availiable methods")
	print("------------------------------------------\n")

	# List available methods
	methods= ["sum","sort","path","equation","reverse","Square"]
	for Method in methods:
		print(Method)

	# Prompt user to select a method
	print("\n------------------------------------------\n")
	method=input("Method :")

	# Generating root method
	#create Root Element
	root = ET.Element("envelope")

	# Sum method
	if method=="sum":
		# Add method name to XML tree
		method_item = ET.SubElement(root, "method")
		method_item.text=method

		# Prompt user to enter number of elements to sum
		total_elm=int(input("Total no.of elment to sum :"))
		Elms=[]
		# Loop through each element and add to XML tree
		for elm in range(1,total_elm+1):
			Num=input("enter number {} :".format(elm))
			arg_item = ET.SubElement(root, "arg")
			arg_item.text=Num
	
	# Sort method
	if method=="sort":
		# Add method name to XML tree
		method_item = ET.SubElement(root, "method")
		method_item.text=method

		# Prompt user to enter number of elements to sort
		total_elm=int(input("Total no.of elment to sort :"))
		Elms=[]
		# Loop through each element and add to XML tree
		for elm in range(1,total_elm+1):
			Num=input("enter number {} :".format(elm))
			arg_item = ET.SubElement(root, "arg")
			arg_item.text=Num
	
	# Square method
	if method=="square":
		# Add method name to XML tree
		method_item = ET.SubElement(root, "method")
		method_item.text=method
		# Prompt user to enter a number to square
		Num=input("enter number to square :")
		# Add number to XML tree
		arg_item = ET.SubElement(root, "arg")
		arg_item.text=Num
	
	# Reverse method
	if method=="reverse":
		# Add method name to XML tree
		method_item = ET.SubElement(root, "method")
		method_item.text="reverse"
		# Prompt user to enter a string to reverse
		Str_=input("enter String to Reverse :")
		# Add string to XML tree
		arg_item = ET.SubElement(root, "arg")
		arg_item.text=Str_
	
	# Equation method
	if method=="equation":
		# Add method name to XML tree
		method_item = ET.SubElement(root, "method")
		method_item.text=method
		# Prompt user to enter an equation
		Eq_=input("Enter Equation :")
		eq_list=list(Eq_)
		# Loop through each element in the equation and add to XML tree
		for elm in eq_list:
			arg_item = ET.SubElement(root, "arg")
			arg_item.text=elm

	# Path method
	if method=="path":
		# Add method name to XML tree
		method_item = ET.SubElement(root, "method")
		method_item.text=method
		# Prompt user to enter the number of nodes
		Total=int(input("Enter no.of nodes :"))
		# Loop through each node and add to XML tree
		for n in range(Total):
			node_item = ET.SubElement(root, "node")
			# Prompt user to enter name of node such as A
			Node_=input("Enter node (such as 'A'): ")
			#add this as subelement in XML tree with <name></name>
			name_item = ET.SubElement(node_item, "name")
			# name of node will be set now in XML 
			name_item.text=Node_
			# Each node has connected node
			# you have to enter connected nodes for selected node such as 'A' is connected to B. 
			# A->B
			adj_nodes=input("Enter connected nodes of node {} (Format : B,E,D):".format(Node_))
			connected=adj_nodes.split(',')
			# now it will enter argument in each XML. 
			# arguments are actually a connected node on backend
			# each node have connected node
			for i in connected: # i is connected node to selected node 
				arg_item = ET.SubElement(node_item, "arg")
				arg_item.text=i

		print("--------------------------------------------\n")
		# enter start node
		start=input("Enter start node :")
		# enetr end node
		# end node is target node where we want to go and find shortest path to it  
		end=input(" enter destination node :")
		# start node will be added in XML tree 
		start_item=ET.SubElement(root, "start")
		# name of start node in XML
		start_item.text=start

		end_item=ET.SubElement(root, "end")
		end_item.text=end

			

	# create the XML tree
	tree = ET.ElementTree(root)

	# write the XML to a file
	tree.write("data.xml")


# Loop runs indefinitely until program is exited
while True:

    # Prompt user to select a method and handle invalid input
    try:
        Selection=int(input("Select any of following method :\n1. Select xml File.\n2. Generate your own xml\n3. Exit\n\nCHOICE(In Number) :"))
    except:
        print("Invalid Selection")
        exit(0)

    # Create an empty list to store file contents
    Lines=[]

    # Handle user selection
    if Selection==1:
        filename=ava_files() # Get filename of an available xml file
    elif Selection==2:
        ava_methods() # Display available xml creation methods
        filename="data.xml" # Use default filename for generated xml
    elif Selection==3:
        exit() # Exit program
    else: 
        print("Invalid Selection")
        
    # Read contents of selected file into a list and store in a dictionary
    with open(filename,'r') as f:
        Lines=f.readlines()

    data={"filename":filename,"Lines":Lines}
    encoded_data=json.dumps(data)

    # Create a socket and connect to a command and control server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 1337))
    s.send(bytes(encoded_data,encoding="utf-8"))
    s.close()

    # Create a TCP socket and listen on localhost port 1447
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 1447))
    s.listen(1)
    check={} # Create an empty dictionary to store incoming data from the server

    while True:

        # Establish a connection with a client
        clientsocket, client_ip = s.accept()
        print("\n[+] received a data from -> {}".format(client_ip))

        # Receive encoded data from client and decode it
        while True:
            encoded_data = clientsocket.recv(4096)
            if not encoded_data:
                clientsocket.close()
                break
            else:
                check=encoded_data.decode("utf-8")
                
        # Exit the inner loop once data has been received and decoded
        break

    # Load decoded data into a dictionary and write it to a file
    reply=json.loads(check)
    with open("result.xml",'w') as f:
        f.write(reply["xml"])

    # Parse the XML data and print out the contents
    tree=ET.parse("result.xml")
    root=tree.getroot()
    for item in root.findall('./arg'):
        string=(item.text.encode("utf-8"))
        print("\nANSWER :{}".format(string.decode("utf-8")))
    
    print("\n---------------------------------------\n\n")

