import socket

#Step 1: Init Socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#Step 2: Get URL input
uri = input('Enter the URI you want to connect to: ')

#Step 3: Establish TCP connection to server
uri = uri.split('/', 3)
file = uri[3]

uri = uri[2].split(':', 1)
ip = uri[0]
port = int(uri[1])

serverAddress = (ip,port)

clientSocket.connect(serverAddress)
#Step 4: Send HTTP Request
request = b"GET /"
request += file.encode()
request += b" HTTP/1.1\r\n"
request += b"Host: " 
request += ip.encode()+b":"+str(port).encode()
request += b"\r\n"  # Sets html header
request += b"Connection: close\r\n\r\n"  
clientSocket.send(request)
#Step 5: Receive data from clientSocket
response = clientSocket.recv(1024)
response = response.decode() #Decodes response
#Parse the HTTP Response
header, _, body = response.partition('\r\n\r\n') #Splits headers from the body

status_line = header.splitlines()[0] #Status code is in first line of header (HTTP/1.1 200 OK)
status_code = status_line.split(" ", 1)[1] #First line is split by spaces, status code is the code in middle

print(f"The Status Code Is: {status_code}\n") #Print the status code and the body
print("HTTP Body:")
print(body)


#Step 6: Close socket
clientSocket.close()