from RSA_algorithm_sign import *

input_file = input("Nhập đường dẫn file cần ký: ").strip()
with open(input_file, 'rb') as f:
    data = f.read()

p, q, n, phi, e, d = generate_keys(min_prime = 100000000000, max_prime = 700000000000)

print("-" * 100)
print("Thông tin khóa:")
print(f"p = {p}")
print(f"q = {q}")
print(f"n = {n}")
print(f"phi(n) = {phi}")
print(f"e = {e}")
print(f"d = {d}")
print(f"-> Khóa ký: {d, n}")
print(f"-> Khóa kiểm thử: {e, n}")

# Lưu thông tin khóa kiểm thử
public_key = {
    "e": e, 
    "n": n, 
}

with open("public_key.txt", 'w') as f:
    for k, v in public_key.items():
        f.write(f"{k}:{v}\n")
print("Thông tin khóa kiểm thử được lưu tại public_key.txt")

signature = sign(data, d, n)
with open("signature.txt", 'w') as f:
    f.write(str(signature))
print("Đã ký file và lưu chữ ký vào signature.txt")
print("-" * 100)