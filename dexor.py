def xor_decrypt(encrypted_message, key):
    # Convertir le message chiffré (en hexadécimal) et la clé en bytes
    encrypted_bytes = bytes.fromhex(encrypted_message)
    key_bytes = key.encode()
    
    # Déchiffrer chaque byte du message chiffré avec la clé en utilisant XOR
    decrypted_bytes = bytes([encrypted_byte ^ key_bytes[i % len(key_bytes)] for i, encrypted_byte in enumerate(encrypted_bytes)])
    
    # Retourner le message déchiffré en tant que chaîne de caractères
    return decrypted_bytes.decode()

# Exemple d'utilisation
encrypted_message = "07001006"
key = "secret"
decrypted_message = xor_decrypt(encrypted_message, key)
print("Message déchiffré :", decrypted_message)
