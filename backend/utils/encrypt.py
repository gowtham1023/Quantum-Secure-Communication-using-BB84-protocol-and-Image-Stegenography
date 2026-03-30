from utils.qkd import generate_qkd_key

def encrypt_message(message):
    message_bytes = message.encode()

    # Generate QKD key (8 bits per character)
    key_bits = generate_qkd_key(len(message_bytes) * 8)

    # Convert bit string → bytes
    key_bytes = []
    for i in range(0, len(key_bits), 8):
        key_bytes.append(int(key_bits[i:i+8], 2))

    key_bytes = bytes(key_bytes)

    # XOR encryption
    encrypted_bytes = bytes([
        message_bytes[i] ^ key_bytes[i]
        for i in range(len(message_bytes))
    ])

    # Convert encrypted bytes to hex string (for storage)
    encrypted_hex = encrypted_bytes.hex()

    return encrypted_hex, key_bits