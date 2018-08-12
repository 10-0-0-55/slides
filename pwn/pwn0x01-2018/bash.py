#!/usr/bin/env python
# -*-coding=utf-8-*-
from pwn import *

io = remote("hackme.inndy.tw",7709)
elf = ELF("./bash")

io.interactive()
io.close()
