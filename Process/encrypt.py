import hashlib

def encrypt(value):
     value_encrypted=hashlib.sha256(str(value).encode()).hexdigest()
     return value_encrypted