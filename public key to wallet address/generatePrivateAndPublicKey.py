from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend

def generatePrivateAndPublicKey():
    privateKey = ec.generate_private_key(
        ec.SECP256K1(), default_backend())  # B
    publicKey = privateKey.public_key()
    return privateKey, publicKey