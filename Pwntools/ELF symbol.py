from pwn import *

e = ELF('./example') # './example' ELF 파일을 로드한다.

print(hex(e.symbols['write']))  # 'write' 심볼의 주소
print(hex(e.symbols.write))      # 'write' 심볼의 주소, 속성 접근