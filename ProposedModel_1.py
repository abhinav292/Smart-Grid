import hashlib

from twofish import Twofish

# Encryption
# TWOFISH
T = Twofish(b'*secret*')
x = T.encrypt(b'YELLOWSUBMARINES')
print("Encrypted Message: ",x)

# SHA-256
m = hashlib.sha256()
m.update(x)
digestMessage = m.digest()
print("Message Digest", digestMessage)
print(m.digest_size)
print(m.block_size)


# Decryption
print(T.decrypt(x).decode())
