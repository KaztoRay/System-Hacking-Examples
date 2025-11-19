from pwn import *

context.arch = 'amd64'  # 아키텍처를 'amd64'로 설정한다.

machine_code = asm('mov eax, 0') # 'mov eax, 0' 어셈블리 코드를 기계어로 변환한다.
print(machine_code)  # 변환된 기계어를 출력한다.

assembly_code = disasm(machine_code) # 기계어를 다시 어셈블리 코드로 변환한다.
print(assembly_code)  # 변환된 어셈블리 코드를 출력한다