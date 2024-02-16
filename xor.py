def xor_encrypt(message, key):
    # Convertir le message et la clé en bytes
    message_bytes = message.encode()
    key_bytes = key.encode()
    
    # Chiffrer chaque byte du message avec la clé en utilisant XOR
    encrypted_bytes = bytes([message_byte ^ key_bytes[i % len(key_bytes)] for i, message_byte in enumerate(message_bytes)])
    
    # Retourner le message chiffré en tant que chaîne de caractères
    return encrypted_bytes.hex()  # Convertir les bytes en hexadécimal pour faciliter le stockage et la lecture

# Exemple d'utilisation
message = ""
key = "Elouan"
encrypted_message = xor_encrypt(message, key)
print("Message chiffré :", encrypted_message)
