"""
소켓생성

접속시도

데이터 송/수신
접속종료
"""

import socket
print("1. 소켓생성")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("3. 접속시도")
sock.connect(("127.0.0.1", 12000))

print("5. 데이터 송/수신")
sock.sendall("hello socket programing".encode())

print("6. 접속종료")
sock.close()
