from pwn import *

s8 = 0x41
s16 = 0x4142
s32 = 0x41424344
s64 = 0x4142434445464748

print(p8(s8))
print(p16(s16))
print(p32(s32))
print(p64(s64))

s8 = b"A"
s16 = b"AB"
s32 = b"ABCD"
s64 = b"ABCDEFGH"

print(hex(u8(s8)))
print(hex(u16(s16)))
print(hex(u32(s32)))
print(hex(u64(s64)))