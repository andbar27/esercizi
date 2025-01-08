
# creazione environment, per evitare che ubuntu non vi faccia installare la libreria di crittografia
# python -m venv .venv
# e poi:
# . .venv/bin/activate
# e poi fare pip install pycryptodome
#

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64


# # Per importare una chiave pubblica
# keyDER = base64.b64decode(pubkey)
# seq = base64.asn1.DerSequence()
# seq.decode(keyDER)
# keyPub = RSA.construct((seq[0], seq[1]))

# # Per iniziare generiamo una coppia di chiavi e le stampiamo
# # Generating RSA Key Pair
# # Una volta stampate, non serve più

# key_pair = RSA.generate(2048)       # Crea una coppia di chiavi pubbliche e private a 2048 bit
# print(key_pair.export_key())      
# public_key = key_pair.publickey()   # prendo la chiave pubblica
# print(public_key.export_key())
# exit(0)

# sPriv = key_pair.export_key()
# sPub = key_pair.publickey().export_key()

# Abbiamo generato le seguenti chiavi con il codice precedente, ora commentato per non generarne di nuove
sPriv = "-----BEGIN RSA PRIVATE KEY-----\nMIIEpAIBAAKCAQEAugWmXdrbIrSqX4QYFnONN9rBjXRZtyOG1eSL1kdv0Zz8YUDv\nPOZbQfj/0UfmyXW1VWIYuK7H8z8mLrOMhRLdDZazXYdkeUUljIT8CSsB5moIETDR\nOSm/XEUUO24lB7+pxR40KhEtJze0RAo5falegbcza//SPnffy1jAta8m91TvcJ5b\nguRnyMUFGWGvv7AkBRMwpBlXrV0gKxmIhJdVYHUk35szjUjL294jtAXQ1KL5zehu\nDY6gZr8l0Xpyd79fNLsvY+SbZBjLfCLfWy9J20BP+w0wrYYJ+bsnLzgbtyaIAsmI\nzfL8PbQC/lR6zGlSfE2JJmy9+NXbr/+eCOY6+QIDAQABAoIBACDYeApo5xn+6/lP\nDeDC+Oukktnq8h9h5MA2KVHFzdLlZPO4HzXx16mzsVnO2At43vKLTmGnrNMAsrl6\nxwRFMyZf1l5clmtKQAnKfmURBLYeQTvl0n+FJU6BvQOMXHn8h9mwDlZiL4aV8Zy0\n8HdFdVQymKAIbONOT8PsMSSzX0460UlyTYYB8DSmpy6CVBONsgK3OgyTMjrKyvw3\nA8msw8ydtsRnS2P4PIag1pqWI8pbiLGMtF6dikZKLuS03jTaEFT5zni3izlha32f\nZOHxNUL7a1p9fTG7jDAKL/fAywWbJUELM8MBjUKtC4wKKOWwkWhhfxbHIC0CfM7o\nuu29550CgYEAuuJbp23YU9Gx0zmArXmRgeD9JMoymIRoRuJiCXIT5zfhAFmMFg6o\nWShHuLTQCxl9a2AE9POzwLeeC6gbZO4ym/MDdyynJMgkpKU/zlReaA2wHhTlr99h\nzQ2t4ZBVyE9SQouFNiVnhTtj/HKvHg9zz+EaV+jKbk3N/Oe8DYB4q5UCgYEA/tGq\nuF3/g1XHzGB6kpyJWj/NAHqYpAx3ncSVI7kQZcsN189jrcYi0tbdjen45gk2BpOZ\nZYEPXkCtKdO3iP0sqDMYz/g74JcgtFYOob3FFJ1s7HaFOPTXEdo9fQ/SKh2TYIjW\nw4kbWJAeaQBW4JlgDTfSHMmjo7zH3KCpxpRjmNUCgYEAkafw9Yq4i4OpTE7KCurw\nTMEVrAHn81VnjK/O5zvBZXn45PPmKh7ceTjaxYwvhickyHZ7BouWswKprL4mM8Ev\nMrryHYVw9EsFvEmLdH3vYrwgYyG4bx30tQQPXPnI0il4nKLvfWcjywSiBlVARXaX\nthLlHFU0yUnc3VukBwX1hw0CgYAIm8Cutc45+53iU6gQZ+Vj/R/J0lpxwFISLF/1\ncv0Q00lGbyUo67aldMjLUIouC0Wd90KJYVDJmFnBPfvHTvZBQGioLfSn47MhJH8e\nC7Eqvx685kwd3nedjMfi/7PT5GfkLPtEY89esI+2cGJ+9+98wtQAUPeMQoZl96+E\nm+K5eQKBgQCYMb+1FI/cIaHGy4E/kEAbch5c82FS5JYaaqYXh7MLGMoovPvSyK+8\nTE02EGz3A22k3qjzTh+p1zxoSqnQA1ExYHoPUQY8fFEjt4tETZiGdYZHcWuFKE1v\nE7na5Ifs80fEpvBLnsA5cRpGrHOEBBmUMEvOxXZZwLvw6TR6pEHHCw==\n-----END RSA PRIVATE KEY-----"
sPub = "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAugWmXdrbIrSqX4QYFnON\nN9rBjXRZtyOG1eSL1kdv0Zz8YUDvPOZbQfj/0UfmyXW1VWIYuK7H8z8mLrOMhRLd\nDZazXYdkeUUljIT8CSsB5moIETDROSm/XEUUO24lB7+pxR40KhEtJze0RAo5fale\ngbcza//SPnffy1jAta8m91TvcJ5bguRnyMUFGWGvv7AkBRMwpBlXrV0gKxmIhJdV\nYHUk35szjUjL294jtAXQ1KL5zehuDY6gZr8l0Xpyd79fNLsvY+SbZBjLfCLfWy9J\n20BP+w0wrYYJ+bsnLzgbtyaIAsmIzfL8PbQC/lR6zGlSfE2JJmy9+NXbr/+eCOY6\n+QIDAQAB\n-----END PUBLIC KEY-----"

# Ora dobbiamo ricreare le chiavi a partire da queste due stringhe
key_pair = RSA.import_key(sPriv)    #trasforma da stringa a chiave effettiva
public_key = RSA.import_key(sPub)


# Function to encrypt message
def encrypt_message(message, pub_key):
    cipher = PKCS1_OAEP.new(pub_key)
    encrypted_message = cipher.encrypt(message.encode("utf-8"))
    return base64.b64encode(encrypted_message).decode("utf-8")


# Function to decrypt message
def decrypt_message(encrypted_message, priv_key):
    cipher = PKCS1_OAEP.new(priv_key)
    decrypted_message = cipher.decrypt(base64.b64decode(encrypted_message))
    return decrypted_message.decode("utf-8")


# Example usage
message = "This is a secret message"
encrypted_message = encrypt_message(message, public_key)
decrypted_message = decrypt_message(encrypted_message, key_pair)

print("Original Message:", message)
print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)
