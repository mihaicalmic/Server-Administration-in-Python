
from dns_client import webPC
import socket as sk                                         # Import socket and call it sk, avoid conflicts
import re


server_socket = sk.socket(sk.AF_INET,sk.SOCK_STREAM)        # Create an ipv4 tcp socket
server_socket.setsockopt(sk.SOL_SOCKET, sk.SO_REUSEADDR, 1) # Release the socket when the program is over

server_socket.bind(('localhost', 7777))                     # Use port 7777 for your server on the local machine
server_socket.listen(1)                                     # Set port to listen for connctions
#print("Server started and is listening on Port 7777")       # Print so you know the program started

connection, client_address = server_socket.accept()         # Accept conction
#print("Accepted connection from Client:", client_address)   # Display message when connction established

while True:                                                 # Create an infinite loop to keep the server on and until its brocken
    data_in = connection.recv(1024)                         # Receive the data
    data = data_in.decode()                              # Reformat the data from binary to normal text
    #print("Received from client:", message)                 # Print any messages recived that were decoded
    
                             # Check to see if the decoded text matches the pattern.
    pattern = r'/*\d\.'
    match = re.search(pattern, data)
    if match:
        message = webPC.getURL(data)
    else:
        message = webPC.getIP(data)
        
        

    # Exit the infinite loop if the above condittion are true
    data_out = message.encode()                             # Encode and store the data received into variable data_out
    connection.send(data_out)                               # Send the varibale data_out
    break
    
#connection.shutdown(sk.SHUT_RDWR)                            # Stop the server from listening
#connection.close()                                          # Close the connction

#server_socket.shutdown(sk.SHUT_RDWR)                        # Stop the socket from reciving anything
#server_socket.close()                                       # Close the socket

  
