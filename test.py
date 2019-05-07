import hashlib
import base64

str = "Amsterdam"

hash = hashlib.sha1(str.encode())

g = base64.urlsafe_b64encode(hash.digest()[:8])

print(hash.digest()[:8])
print(8%8)