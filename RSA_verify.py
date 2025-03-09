from RSA_algorithm_sign import *

input_file = input("Nhập đường dẫn file cần ký: ").strip()
with open(input_file, 'rb') as f:
    data = f.read()

public_key = {}
with open("public_key.txt", 'r') as f:
    for line in f:
        k, v = line.strip().split(':')
        public_key[k] = v

n = int(public_key["n"])
e = int(public_key["e"])

with open("signature.txt", 'r') as f:
    signature = int(f.read().strip())

if verify(data, signature, e, n):
    print("Chữ ký HỢP LỆ!")
else:
    print("Chữ ký KHÔNG hợp lệ!")