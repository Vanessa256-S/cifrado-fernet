# Fernet Encryption and Decryption

Python script that demonstrates **symmetric password encryption** using the **Fernet** algorithm, requesting a key from the user, encrypting it, and then decrypting it.

Developed for the **Ethical Hacking — 9th Semester** course.

---

## Purpose

Encryption is one of the fundamental pillars of information security. This script shows:

- **How to protect sensitive data**: passwords should never be stored in plain text
- **Symmetric encryption in practice**: the same key is used for encryption and decryption
- **Why Fernet is secure**: it combines AES-128 in CBC mode with HMAC-SHA256 to guarantee **confidentiality** and **integrity**
- **The importance of key management**: without the key, the data is unrecoverable

---

## What is Fernet?

**Fernet** is an authenticated symmetric encryption scheme defined in Python's `cryptography` library. It guarantees:

| Property | Mechanism |
|---|---|
| **Confidentiality** | AES-128 in CBC mode |
| **Integrity** | HMAC with SHA-256 |
| **Authenticity** | Message signing with timestamp |
| **Tamper resistance** | The token is invalid if modified |

---

## How does it work?

```
Start
  └─ Generate random Fernet key (256 bits in Base64)
      └─ Ask user for password
          └─ Encrypt password → unreadable token
              └─ Decrypt token → original text
                  └─ Display key, encrypted token, and result
                      └─ End
```

### Functions

| Function | What it does |
|---|---|
| `generate_key()` | Generates a random 32-byte key encoded in Base64 |
| `encrypt_password(password, key)` | Encrypts the text with the Fernet key |
| `decrypt_password(encrypted_password, key)` | Decrypts the token and returns the original text |

---

## Sample output

```
Enter the password: MiContraseña123!

--- Encryption Results ---
Encryption key: dGhpcyBpcyBhIHZlcnkgbG9uZyBrZXkgZm9yIGZlcm5ldA==
Encrypted password: gAAAAABmX3k2...  (encrypted unreadable token)
Decrypted password: MiContraseña123!
```

---

## Technologies

| Library | Usage |
|---|---|
| `cryptography.fernet` | Implementation of the Fernet encryption scheme |

### Installation

```bash
pip install cryptography
```

---

## How to run it

```bash
python desincriptar_fernet.py
```

---

## Important security considerations

> **The key is the most important part.** If it is lost, the encrypted data is unrecoverable.

In a real system, the Fernet key should be:
- Stored in a **secrets manager** (e.g., AWS Secrets Manager, HashiCorp Vault)
- **Never** hardcoded in the source code
- Rotated periodically to minimize the impact of a leak

---

## Applied security concepts

- **Symmetric encryption**: same key for encryption and decryption (as opposed to asymmetric like RSA)
- **Authenticated encryption**: guarantees that the message has not been altered (AEAD)
