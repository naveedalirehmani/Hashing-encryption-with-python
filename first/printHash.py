import bcrypt
import hashlib

def printHash(name):
    nameInBytes = name.encode()
    print("Your name in bytes ",nameInBytes)
    for bytes in nameInBytes:
        print(bytes)

    # MD5
    md5_hash = hashlib.md5(name.encode()).hexdigest()
    # SHA-1
    sha1_hash = hashlib.sha1(name.encode()).hexdigest()
    # SHA-256
    sha256_hash = hashlib.sha256(name.encode()).hexdigest()
    # SHA-512
    sha512_hash = hashlib.sha512(name.encode()).hexdigest()
    # SHA-3
    sha3_hash = hashlib.sha3_256(name.encode()).hexdigest()
    # BLAKE2
    blake2_hash = hashlib.blake2s(name.encode()).hexdigest()
    # RIPEMD-160
    ripemd160_hash = hashlib.new('ripemd160', name.encode()).hexdigest()

    # Print the hashes
    print("MD5:", md5_hash)
    print("SHA-1:", sha1_hash)
    print("SHA-256:", sha256_hash)
    print("SHA-512:", sha512_hash)
    print("SHA-3:", sha3_hash)
    print("BLAKE2:", blake2_hash)
    print("RIPEMD-160:", ripemd160_hash)

    # generating bcrypt of your name
    salt = bcrypt.gensalt()
    bcryptHash = bcrypt.hashpw(nameInBytes,salt)

    print("bcrypt Hash:", bcryptHash)