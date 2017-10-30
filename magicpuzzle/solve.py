#!/usr/bin/python -u
from pwn import *
import time
import base64
import subprocess
import angr
import logging
context.arch = "amd64"
ip = "0"
port = 5566
s = remote(ip, port)
print(s.recvuntil("base64"))
for i in range(2):
    if i:
        s.recvuntil('GJ!')
    program = s.recvuntil("0th")
    program = program[:program.find("0th")].strip()
    print(s.recv())
    with open('log','wb') as f:
        f.write(program)
    elf = base64.b64decode(program)
    with open('tmp','wb') as f:
        f.write(elf)
    output = subprocess.check_output("objdump -d -M intel tmp | grep catflag",shell=True).split("\n")[1]
    print(output)
    address = int(output[:output.find(':')],16)
    print(str(address))
    logging.basicConfig(level=logging.DEBUG)
    proj = angr.Project('./tmp', auto_load_libs=False)
    state = proj.factory.blank_state()
    simgr = proj.factory.simgr(state)
    end = address+ 0x400000
    simgr.explore(find=end)
    payload = ''
    if simgr.found:
        payload = simgr.found[0].posix.dumps(0)
        print(payload)
    s.send(payload)
    print("Good")
    time.sleep(1)
s.interactive()
