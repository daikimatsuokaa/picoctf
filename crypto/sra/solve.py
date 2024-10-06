from sage.all import *
from Crypto.Util.number import long_to_bytes

c = 4499547058765796615460255896858961814722144432206694217389610001801619641917
d = 72697768193915129929854234677530693693447583883325099574185332898443393232321
e = 0x10001

# nを求めたい
# kはphi(n)の倍数なのでkの約数を全探索してphi(n)を求め　, その後nを求める
k = e * d - 1

divs = divisors(k)

def is_128bit(x):
    return 2 ** 127 <= x <= 2 ** 128 - 1

print(len(divs))

for div in divs:
    phi = div
    if phi <= d:
        continue
    phi_divs = divisors(phi)
    for phi_div in phi_divs:
        if not is_128bit(phi_div):
            continue
        p = phi_div + 1
        q = phi // phi_div + 1
        if is_prime(p) and is_prime(q) and is_128bit(p) and is_128bit(q):
            n = p * q
            if c < n:
                m = pow(c, d, n)
                print(long_to_bytes(m))
