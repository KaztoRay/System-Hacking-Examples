from pwn import *

p = process('./example')

p.interactive()