import random
import math
import os

# Kiểm tra số nguyên tố
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Sinh số nguyên tố trong khoảng [min_val, max_val]
def generate_prime(min_val, max_val):
    while True:
        p = random.randint(min_val, max_val)
        if is_prime(p):
            return p

# Tìm e sao cho gcd(e, phi) = 1
def find_e(phi):
    while True:
        e = random.randint(3, phi - 1)
        if math.gcd(e, phi) == 1:
            return e

# Tính nghịch đảo modulo: d sao cho d*e ≡ 1 (mod phi)
def modinv(a, m):
    def egcd(a, b):
        if a == 0:
            return (b, 0, 1)
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)
    g, x, _ = egcd(a, m)
    return x % m


# Sinh khóa RSA
def generate_keys(min_prime=10000, max_prime=70000):
    p = generate_prime(min_prime, max_prime)
    q = generate_prime(min_prime, max_prime)
    while p == q:
        q = generate_prime(min_prime, max_prime)
        
    n = p * q
    phi = (p - 1) * (q - 1)
    e = find_e(phi)
    d = modinv(e, phi)
    return p, q, n, phi, e, d

# Ký trực tiếp tính m^d mod n
def sign(m, d, n):
    m_int = int.from_bytes(m, 'big')
    sig = pow(m_int, d, n)
    return sig

# Kiểm tra chữ ký  
def verify(m, sig, e, n):
    m_int = int.from_bytes(m, 'big')
    m_check = pow(sig, e, n)
    print(f"m_int = {m_int}")
    print(f"m_check = {m_check}")
    return m_check == m_int