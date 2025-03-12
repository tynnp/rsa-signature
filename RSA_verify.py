from RSA_sign_algorithm import *

# Lấy nội dung chữ ký số
print("-" * 100)
signature_file = input("Nhập đường dẫn đến file chữ ký số: ")
with open(signature_file, "r") as f:
    signature = json.load(f)
rsa_signature = signature["signature"]

# Lấy nội dung file cần kiểm thử chữ ký số
file_path = input("Nhập đường dẫn đến file cần kiểm thử chữ ký số: ")
with open(file_path, "rb") as f:
    plaintext_bytes = f.read()

# Lấy nội dung khóa công khai để kiểm thử
pub_file = "public_key.json"
with open(pub_file, "r") as f:
    public_key = json.load(f)

e = public_key["e"]
n = public_key["n"]

# Thực hiện kiểm thử chữ ký
result = verify(plaintext_bytes, rsa_signature, e, n)
if result:  
    print("Chữ ký hợp lệ!")
else:
    print("Chữ ký không hợp lệ!")
print("-" * 100)