import socket

msg = "\r\n I love computer networks!"
endMsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server) and call it mailserver
mailServer = "smtp.gmail.com"
port = 587
# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((mailServer, port))
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')
# Send HELO command and print server response.
heloCommand = 'HELO client.net\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
# Send MAIL FROM command and print server response.
# Fill in start
mailFromCommand = 'MAIL FROM "test@client.net"\r\t'
clientSocket.send(mailFromCommand.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)
if recv2[:3] != '250':
    print('250 reply not received from server.')
# Fill in end
# Send RCPT TO command and print server response.
# Fill in start
# Fill in end
# Send DATA command and print server response.
# Fill in start
# Fill in end
# Send message data.
# Fill in start
# Fill in end
# Message ends with a single period.
# Fill in start
# Fill in end
# Send QUIT command and get server response.
# Fill in start
# Fill in end
