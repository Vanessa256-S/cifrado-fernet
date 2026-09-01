from cryptography.fernet import Fernet


def generate_key():
    """Generate and return a new Fernet encryption key."""
    return Fernet.generate_key()


def encrypt_password(password, key):
    """Encrypt the provided password using the Fernet key."""
    cipher = Fernet(key)
    encrypted_password = cipher.encrypt(password.encode())
    return encrypted_password


def decrypt_password(encrypted_password, key):
    """Decrypt the encrypted password using the Fernet key."""
    cipher = Fernet(key)
    decrypted_password = cipher.decrypt(encrypted_password)
    return decrypted_password.decode()


def main():
    """Run the password encryption and decryption process."""
    encryption_key = generate_key()

    password = input("Enter the password: ")

    encrypted_password = encrypt_password(password, encryption_key)
    decrypted_password = decrypt_password(encrypted_password, encryption_key)

    print("\n--- Encryption Results ---")
    print(f"Encryption key: {encryption_key.decode()}")
    print(f"Encrypted password: {encrypted_password.decode()}")
    print(f"Decrypted password: {decrypted_password}")


if __name__ == "__main__":
    main()
