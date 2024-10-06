from Crypto.PublicKey import RSA
from Crypto.Util.number import long_to_bytes
from sage.all import *

with open('cert', 'r') as cert_file:
    pem_data = cert_file.read()

rsa_key = RSA.import_key(pem_data)

n = rsa_key.n
e = rsa_key.e

factors = factor(n)
p = int(factors[0][0])
q = int(factors[1][0])

print(f'picoCTF{{{p},{q}}}')
print(f'picoCTF{{{q},{p}}}')
