from pwn import *

p = process('./example')

p.send(b'A')    # ./example에 b'A'를 입력한다.
p.sendline(b'A') # ./example에 b'A'+ b'\n'을 입력한다.
p.sendafter(b'hello', b'A') # ./example이 b'hello'를 출력한 후에 b'A'를 입력한다.
p.sendlineafter(b'hello', b'A') # ./example이 b'hello'를 출력한 후에 b'A'+ b'\n'을 입력한다.