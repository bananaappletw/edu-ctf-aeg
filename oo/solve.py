#!/usr/bin/env python
from pwn import *
import base64
import subprocess
ip = "133.130.124.59"
port = 9992
s = remote(ip, port)
print(s.recvuntil("base64"))
program = s.recvuntil("NOW")
program = program[:program.find("NOW")]

elf = base64.b64decode(program)
with open('tmp','wb') as f:
    f.write(elf)
output = subprocess.check_output("objdump -d -M intel tmp | grep DWORD | grep rip",shell=True).split("\n")
for line in output:
    if ',' in line:
        line = line[line.find(",")+1:]
        line = line[:line.find(" ")]
        s.sendline(str(int(line,16)))
s.interactive()
