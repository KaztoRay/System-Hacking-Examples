from pwn import *

p = process("./example")

gdb.attach(p)  # gdb를 사용하여 ./example 프로세스에 연결한다.

sleep(1)  # 1초 동안 대기한다.