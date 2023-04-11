import xml.etree.ElementTree as ET
import json
import socket
import os

def ava_files():
	cwd = os.getcwd()
	print('\nSelect Filename From availaible Filenames:')
	print("------------------------------------------\n")

	# List all files in the current working directory
	files = os.listdir("{}".format(cwd))

	for file in files:print(file)

	print("\n---------------------------------------------")
	filename=input("Filename :")
	return filename


def ava_methods():
	print("select your method from availiable methods")
	print("------------------------------------------\n")
	methods= ["sum","sort","path","equation","reverse","Square"]
	for Method in methods:
		print(Method)
	print("\n------------------------------------------\n")

	method=input("Method :")
	#Generating root method
	
	#create Root Element

	root = ET.Element("envelope")
	
	if method=="sum":
		
		method_item = ET.SubElement(root, "method")
		method_item.text=method

		total_elm=int(input("Total no.of elment to sum :"))
		Elms=[]
		for elm in range(1,total_elm+1):
			Num=input("enter number {} :".format(elm))
			arg_item = ET.SubElement(root, "arg")
			arg_item.text=Num
	

	if method=="sort":
		
		method_item = ET.SubElement(root, "method")
		method_item.text=method

		total_elm=int(input("Total no.of elment to sort :"))
		Elms=[]
		for elm in range(1,total_elm+1):
			Num=input("enter number {} :".format(elm))
			arg_item = ET.SubElement(root, "arg")
			arg_item.text=Num
	

	if method=="square":
		
		method_item = ET.SubElement(root, "method")
		method_item.text=method
		Num=input("enter number to square :")
		arg_item = ET.SubElement(root, "arg")
		arg_item.text=Num

	

	if method=="reverse":
		
		method_item = ET.SubElement(root, "method")
		method_item.text="reverse"

		Str_=input("enter String to Reverse :")
		arg_item = ET.SubElement(root, "arg")
		arg_item.text=Str_	
		
	if method=="equation":
		
		method_item = ET.SubElement(root, "method")
		method_item.text=method
		Eq_=input("Enter Equation :")
		eq_list=list(Eq_)
		for elm in eq_list:
			arg_item = ET.SubElement(root, "arg")
			arg_item.text=elm

	if method=="path":

		method_item = ET.SubElement(root, "method")
		method_item.text=method

		Total=int(input("Enter no.of nodes :"))

		for n in range(Total):
			
			node_item = ET.SubElement(root, "node")
			Node_=input("Enter node (such as 'A'): ")
			name_item = ET.SubElement(node_item, "name")
			name_item.text=Node_
			adj_nodes=input("Enter connected nodes of node {} (Format : B,E,D):".format(Node_))
			connected=adj_nodes.split(',')

			for i in connected:
				arg_item = ET.SubElement(node_item, "arg")
				arg_item.text=i

		print("--------------------------------------------\n")
		start=input("Enter start node :")
		end=input(" enter destination node :")

		start_item=ET.SubElement(root, "start")
		start_item.text=start

		end_item=ET.SubElement(root, "end")
		end_item.text=end

			

	# create the XML tree
	tree = ET.ElementTree(root)

	# write the XML to a file
	tree.write("data.xml")



while True:

	try:
		Selection=int(input("Select any of following method :\n1. Select xml File.\n2. Generate your own xml\n3. Exit\n\nCHOICE(In Number) :"))
	except:
		print("Invalid Selection")
		exit(0)

	Lines=[]

	if Selection==1:
		filename=ava_files()

	elif Selection==2:
		ava_methods()
		filename="data.xml"
	elif Selection==3:
		exit()
	else: 
		print("Invalid Selection")
		

	with open(filename,'r') as f:
		Lines=f.readlines()

	data={"filename":filename,"Lines":Lines}
	encoded_data=json.dumps(data)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# connect to command and control server on port 1337
	s.connect(("127.0.0.1", 1337))
	s.send(bytes(encoded_data,encoding="utf-8"))
	s.close()



	# create TCP socket
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# listen on localhost port 1337
	s.bind(("127.0.0.1", 1447))
	s.listen(1)
	check={}

	while True:

		# establish a connection
		clientsocket, client_ip = s.accept()
		print("\n[+] received a data from -> {}".format(client_ip))
		#open a file with a random name and insert the decoded data into it
		while True:
			# get the encoded data
				encoded_data = clientsocket.recv(4096)
				if  not encoded_data:
					clientsocket.close()
					break
			
				else :
					check=encoded_data.decode("utf-8")
                
                
		break

	reply=json.loads(check)


	with open("result.xml",'w') as f:
		f.write(reply["xml"])

	tree=ET.parse("result.xml")
	root=tree.getroot()

	for item in root.findall('./arg'):
		string=(item.text.encode("utf-8"))
		print("\nANSWER :{}".format(string.decode("utf-8")))
	
	print("\n---------------------------------------\n\n")

