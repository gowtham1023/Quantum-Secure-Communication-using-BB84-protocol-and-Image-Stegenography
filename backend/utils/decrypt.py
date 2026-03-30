def decrypt_message(encrypted_hex, key_bits):

    # Convert hex → bytes
    encrypted_bytes = bytes.fromhex(encrypted_hex)

    # Convert key bits → bytes
    key_bytes = []
    for i in range(0, len(key_bits), 8):
        key_bytes.append(int(key_bits[i:i+8], 2))

    key_bytes = bytes(key_bytes)

    # XOR decryption
    decrypted_bytes = bytes([
        encrypted_bytes[i] ^ key_bytes[i]
        for i in range(len(encrypted_bytes))
    ])

    return decrypted_bytes.decode(errors="ignore")