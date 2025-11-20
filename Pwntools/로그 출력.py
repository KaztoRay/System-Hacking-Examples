from pwn import *

context_log_level = 'debug'  # Pwntools의 로그 레벨을 'debug'로 설정한다.

p = process("./example")

p.recvall()  # p가 출력하는 모든 데이터를 프로세스가 종료될 때까지 받아서 반환한다.