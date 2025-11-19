from pwn import *

p = process('./example')

data = p.recv(1024)  # p가 출력하는 데이터를 최대 1024바이트까지 받아서 data에 저장한다.
data = p.recvline()  # p가 출력하는 데이터를 개행문자를 만날 때까지 받아서 data에 저장한다.
data = p.recvn(5)    # p가 출력하는 데이터를 5바이트만 받아서 data에 저장한다.
data = p.recvuntil(b'hello') # p가 b'hello'를 출력할 때까지 데이터를 수신하여 data에 저장한다.
data = p.recvall()  # p가 출력하는 모든 데이터를 프로세스가 종료될 때까지 받아서 data에 저장한다.