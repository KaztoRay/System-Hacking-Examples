from pwn import *

p = process('./example')

p.close() # ./example 프로세스를 종료한다.