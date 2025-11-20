from pwn import *

context.arch = 'amd64'  # 아키텍처를 'amd64'로 설정한다.
context.arch = 'i386'   # 아키텍처를 'i386'으로 설정한다.
context.arch = 'arm'    # 아키텍처를 'arm'으로 설정한다