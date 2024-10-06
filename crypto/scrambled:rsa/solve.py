from pwn import *
import sys
from sage.all import *
from Crypto.Util.number import bytes_to_long, long_to_bytes

sys.set_int_max_str_digits(10000)

sock = remote('mercury.picoctf.net', 58251)

flag = int(sock.recvline().decode().split(': ')[1].strip())
n = int(sock.recvline().decode().split(': ')[1].strip())
e = int(sock.recvline().decode().split(': ')[1].strip())

sock.recvuntil(b'me: ')
sock.sendline(b'\x01')
c1 = int(sock.recvline().decode().split(': ')[1].strip())

sock.recvuntil(b'me: ')
sock.sendline(b'1')
c2 = int(sock.recvline().decode().split(': ')[1].strip())

print(f'c1 = {c1}')
print(f'c2 = {c2}')

g = gcd(48 ** e - c1, 49 ** e - c2)
print(f'g = {g}')
