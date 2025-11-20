from pwn import *

r = remote("example.com", 1337, typ='udp')