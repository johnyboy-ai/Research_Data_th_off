import hashlib
strg = '0xF9DA3'

print(bin(eval(strg)))


result = hashlib.sha256(str.encode())


print(result)
print(result.hexdigest())

print(hashlib.)