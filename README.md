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
