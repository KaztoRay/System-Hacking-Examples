from pwn import *

s = ssh("dreamhack", "127.0.0.1", port=22, password="dreamhack")
