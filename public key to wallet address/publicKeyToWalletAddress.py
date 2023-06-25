import hashlib
import base58

def publicKeyToWalletAddress(publicKey):

    # public key to sha-256 hash in hexa
    sha256Hash = hashlib.sha256(publicKey).hexdigest()
    
    # sha256Hash to ripemd160Hash in bits
    ripemd160Hash = hashlib.new('ripemd160', sha256Hash.encode()).digest()

    # ripemd160Hash to sha-256 hash in bits
    sha256Hash1 = hashlib.sha256(ripemd160Hash).digest()

    # sha-256 to sha-256 in bits
    sha256Hash2 = hashlib.sha256(sha256Hash1).digest()

    checksum = sha256Hash2[:4]
    
    network_bytes = b'00'
    net_rem_hash = network_bytes+ripemd160Hash
    extended = net_rem_hash+checksum

    wallet_address = base58.b58encode(extended)

    return wallet_address.decode()

