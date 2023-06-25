
from cryptography.hazmat.primitives import serialization

from publicKeyToWalletAddress import publicKeyToWalletAddress
from generatePrivateAndPublicKey import generatePrivateAndPublicKey

GREEN = "\033[32m"
RESET = "\033[0m"

(privateKey, publicKey) = generatePrivateAndPublicKey()

public_bytes = publicKey.public_bytes(
    encoding=serialization.Encoding.X962,
    format=serialization.PublicFormat.UncompressedPoint
)

walletAddress = publicKeyToWalletAddress(public_bytes)

print("wallet address = "+GREEN+walletAddress+RESET)
