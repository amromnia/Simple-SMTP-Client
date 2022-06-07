import base64
import socket
import ssl
# import tkinter as tk
# from tkinter import simpledialog

# root = tk.Tk()

# root.title("Networks Project")
# root.withdraw()

# # the input dialog
# rec_email = simpledialog.askstring(title="Test",prompt="Enter receipient email: ") 
# tmp = simpledialog.askstring(title="Test",prompt="Enter message")
print("SMTP Server starting...\r\n")
rec_email=input("Enter the receipient E-mail: ")
tmp=input("Message: ")

msg = "\r\n"+tmp if tmp else "I love computer Networks!"
endMsg = "\r\n.\r\n"
#rec_email = "asd.sadek@gmail.com"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailServer = "smtp.office365.com"
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
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '250':
    print('250 reply not received from server.')

TLSCommand = 'starttls\r\n'
clientSocket.send(TLSCommand.encode())
recv = clientSocket.recv(1024).decode()
print(recv)

secureSocket = ssl.wrap_socket(clientSocket, ssl_version=ssl.PROTOCOL_TLSv1)

heloCommand = 'HELO client.net\r\n'
secureSocket.send(heloCommand.encode())
recv = secureSocket.recv(1024).decode()
print(recv)
if recv[:3] != '250':
    print('250 reply not received from server.')

authCommand = 'auth LOGIN\r\n'
secureSocket.send(authCommand.encode())
recv = secureSocket.recv(1024).decode()
print(recv)

username = 'smtptesting754@outlook.com'
encodedUsername = base64.b64encode(username.encode())
secureSocket.send(encodedUsername)
secureSocket.send('\r\n'.encode())
recv = secureSocket.recv(1024).decode()
print(recv)
password = 'smtp_test'
encodedPassword = base64.b64encode(password.encode())
secureSocket.send(encodedPassword)
secureSocket.send('\r\n'.encode())
print("sent pass")

recv = secureSocket.recv(1024).decode()
print(recv)

# Send MAIL FROM command and print server response.
mailFromCommand = 'MAIL FROM:smtptesting754@outlook.com\r\n'
secureSocket.send(mailFromCommand.encode())
recv = secureSocket.recv(1024).decode()
print(recv)
if recv[:3] != '250':
    print('250 reply not received from server.')

# Send RCPT TO command and print server response.
RCPTCommand = 'RCPT TO:'+rec_email+'\r\n'
secureSocket.send(RCPTCommand.encode())
recv = secureSocket.recv(1024).decode()
print(recv)
if recv[:3] != '250':
    print('250 reply not received from server.')

# Send DATA command and print server response.

DataCommand = 'DATA\r\n'
secureSocket.send(DataCommand.encode())
recv = secureSocket.recv(1024).decode()
print(recv)
if recv[:3] != '354':
    print('354 reply not received from server.')  # expected reply 354 start mail input or 354 GO AHEAD

# Send message data.
secureSocket.send(msg.encode())
# Message ends with a single period.
secureSocket.send(endMsg.encode())
recv = secureSocket.recv(1024).decode()
print(recv)
if recv[:3] != '250':
    print('250 reply not received from server.')

# Send QUIT command and get server response.
QuitCommand = 'QUIT\r\n'
secureSocket.send(QuitCommand.encode())
recv = secureSocket.recv(1024).decode()
print(recv)
if recv[:3] != '221':
    print('221 reply not received from server.') # expected reply 221 Service closing transmission channel