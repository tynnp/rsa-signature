from RSA_sign_algorithm import *

# Lấy nội dung file cần ký số
print("-" * 100)
file_path = input("Nhập đường dẫn đến file cần ký số: ")
with open(file_path, "rb") as f:
    plaintext_bytes = f.read()

# Lấy nội dung khóa bí mật để ký
priv_file = "private_key.json"
with open(priv_file, "r") as f:
    private_key = json.load(f)

d = private_key["d"]
n = private_key["n"]

# Thực hiện ký số và tạo chữ ký
rsa_signature = sign(plaintext_bytes, d, n)
signature = {
    "signature": rsa_signature
}

# Ghi lại chữ ký số
signature_file = "signature.json"
with open(signature_file, "w") as f:
    json.dump(signature, f, indent=4)
print(f"file chữ ký số được lưu tại {signature_file}", "-" * 100, sep='\n')