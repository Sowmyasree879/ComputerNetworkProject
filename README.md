                                                           CSCI6760 Computer Networks Spring 2023

                                                               An XML-RPC Application


Introduction:

The XML-RPC protocol is a popular internet protocol for client-server communication. This protocol enables a client to call methods on a server and get the results of those calls in XML format. We created an XML-RPC application in this project that uses socket communication to transport XML messages between the client and the server. The client can use the server's methods to compute the square of a given number, the sum of a given list of integers, reversing a given string, sorting a list of integers, solving mathematical equations, and finding the shortest path in a graph.

Methodology:

The Python programming language was utilized to create the XML-RPC application. The socket module is used to communicate between the client and the server using sockets. The xml module is used to decode XML messages, while the OS module is used to execute OS activities such as method invocation. A Python script (command: python server.py) on the server receives an XML message from the client, decodes it to execute method invocation, and then provides the result (as an XML message) to the client. The client has a Python script (command: python client.py) that sends an XML message to the server, then receives the server's response (also in the form of an XML message), decodes it, and displays the result on the screen.
Note: Always start server first. Then start client (command: python client.py). Client will send you different option work according to it.
Logic Flow:
1.The client sends an XML message (in the form of a method invocation) to the server.
2.The server receives the XML message from the client, and decodes it to determine which method to invoke.
3.The server invokes the requested method, passing any necessary arguments.
4.The server computes the result of the method invocation.
5.The server encodes the result as an XML message, and sends it back to the client.
6.The client receives the XML message from the server.
7.The client decodes the XML message to extract the result of the method invocation.
8.The client prints the result on the screen.

Program Flow:

1.The server script (server.py) starts by creating a socket and binding it to a specific port.
2.The server script listens for incoming connections from clients on this port.
3.When a client connects to the server, the server script creates a new thread to handle the client's request.
4.The server script reads the XML message from the client, and decodes it to determine which method to invoke.
5.The server script invokes the requested method, passing any necessary arguments.
6.The server script computes the result of the method invocation.
7.The server script encodes the result as an XML message, and sends it back to the client.
8.The client script (client.py) starts by creating a socket and connecting to the server on a specific port.
9.The client script sends XML message to the server.
10.The client script waits for a response from the server.
11.The client script receives the response from the server, and decodes it to extract the result of the method invocation.
12.The client script prints the result on the screen.

Backend Working of XML-RPC:

The backend of the XML-RPC application consists of the server-side code that receives incoming socket connections from clients, parses the XML requests, invokes the appropriate method based on the request, and sends the result back to the client in an XML response.

The backend working of the application can be explained in the following steps:

1.Setting up the server: The server is set up to listen for incoming socket connections from clients. The server can be set up on any machine with a network connection and a Python environment.

2.Handling incoming socket connections: When a client establishes a socket connection with the server, the server accepts the connection and starts receiving the XML request message from the client.

3.Parsing the XML request: The server parses the XML request message to extract the method name and the input parameters. The xml module in Python can be used for parsing the XML messages.

4.Invoking the method: Based on the method name in the XML request message, the server invokes the appropriate method with the input parameters. The method can be any python file at server side  that takes input parameters and returns a result.

5.Creating the XML response: The server creates an XML response message with the result of the method invocation.

6.Sending the XML response: The server sends the XML response message back to the client over the socket connection.

Program Execution:

Navigate to directory of server in command line.
Execute command (python server.py).
Server is started and listening for connection from client
Now open another terminal and navigate to directory of client in command line.
Now execute command (python client.py). Note that server is already running on another terminal.
After you execute command. Client will show you following menu on terminal:
1. select xml file
2. generate xml file
3. exit
If you click option ‘1’ it will show you pre-generated XML files.
A file can be selected from the pre-generated files and it will be executed.
Note in this way you can select any XML file which are pre-generated.
XML file handles all methods such as square, sum, equation calculator, shortest path, reverse string, sorting. In the screenshot I have shown only sum method but you all options.
If you want to generate your own XML file. Select option ‘2’.
select any method for which you wanted to generate xml and give the inputs for the method to be executed.
This way we can generate any xml file for any method that has been choosen.

Conclusion:

In this project, we have implemented an XML-RPC application that uses socket communication to transfer XML messages between the client and the server. We have shown how to implement several different methods on the server, including methods for computing the square of a given number, computing the sum of a given list of integers, reversing a given string, sorting a list of integers, solving mathematical equations, and finding the shortest path in a graph. We have demonstrated how the client can invoke these methods by sending XML messages to the server, and how the server responds back to the client.
