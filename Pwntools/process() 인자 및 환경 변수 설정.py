from pwn import *

p = process(["./example", "AAAA"], env={"LD_PRELOAD":"./libc.so.6"})