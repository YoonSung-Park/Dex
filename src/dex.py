from socket import *

HOST = 'mail.nefacility.com'
PORT = 25
BUF_SIZE = 1024
ADDR = (HOST,PORT)

client_socket = socket(AF_INET, SOCK_STREAM)

client_socket.connect(ADDR) # 메일서버 연결

# 연결 직후
msg = client_socket.recv(BUF_SIZE).decode()
print(msg)

# HELO 전송
client_socket.sendall('HELO mail.nefacility.com\r\n'.encode())
msg = client_socket.recv(BUF_SIZE).decode() # 데이터 수신
print(msg)

# MAIL FROM 전송
client_socket.sendall('MAIL FROM:<devhudi@gmail.com>\r\n'.encode())
msg = client_socket.recv(BUF_SIZE).decode()
print(msg)

# RCPT TO 전송
client_socket.sendall('RCPT TO:<rocexen287@nefacility.com>\r\n'.encode())
msg = client_socket.recv(BUF_SIZE).decode()
print(msg)

# DATA 전송
client_socket.sendall('DATA\r\n'.encode())
msg = client_socket.recv(BUF_SIZE).decode()
print(msg)

# 헤더 및 본문 전송
client_socket.sendall('From: "devHudi" <devhudi@gmail.com>\r\n'.encode())
client_socket.sendall('To: "temp" <rocexen287@nefacility.com>\r\n'.encode())
client_socket.sendall('Subject: Hello, SMTP!\r\n'.encode())
client_socket.sendall('\r\nThis is test mail from python.\r\n.\r\n'.encode())
msg = client_socket.recv(BUF_SIZE).decode()
print(msg)

# 연결 종료
client_socket.close()