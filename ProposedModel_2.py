from xtwine import Twine
import hashlib
# Encryption
# TWINE
twine = Twine(key_size=0x50)
ciphertext = twine.encrypt("hello world")
print(ciphertext)

# SHA-256
m = hashlib.sha256()
m.update(ciphertext.encode('utf-8'))
digestMessage = m.digest()
print("Message Digest", digestMessage)
print(m.digest_size)
print(m.block_size)

# Decryption
plaintext = twine.decrypt(ciphertext)
print(plaintext)