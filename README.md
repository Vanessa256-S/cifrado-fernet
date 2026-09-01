# 🔐 Cifrado y Descifrado con Fernet

Script en Python que demuestra el **cifrado simétrico de contraseñas** usando el algoritmo **Fernet**, solicitando una clave al usuario, cifrándola y luego descifrándola.

Desarrollado para el curso de **Ética Hacking — 9° Semestre**.

---

## 🎯 Propósito

El cifrado es uno de los pilares fundamentales de la seguridad informática. Este script muestra:

- 🔒 **Cómo proteger datos sensibles**: las contraseñas nunca deben guardarse en texto plano
- 🔑 **Cifrado simétrico en la práctica**: misma clave para cifrar y descifrar
- 🛡️ **Por qué Fernet es seguro**: combina AES-128 en modo CBC con HMAC-SHA256 para garantizar **confidencialidad** e **integridad**
- ⚠️ **La importancia de gestionar las claves**: sin la clave, los datos son irrecuperables

---

## 🔬 ¿Qué es Fernet?

**Fernet** es un esquema de cifrado simétrico autenticado definido en la librería `cryptography` de Python. Garantiza:

| Propiedad | Mecanismo |
|---|---|
| **Confidencialidad** | AES-128 en modo CBC |
| **Integridad** | HMAC con SHA-256 |
| **Autenticidad** | Firma del mensaje con timestamp |
| **Resistencia a manipulación** | El token es inválido si es modificado |

---

## ⚙️ ¿Cómo funciona?

```
Inicio
  └─ Generar clave Fernet aleatoria (256 bits en Base64)
      └─ Solicitar contraseña al usuario
          └─ Cifrar contraseña → token ilegible
              └─ Descifrar token → texto original
                  └─ Mostrar clave, token cifrado y resultado
                      └─ Fin
```

### Funciones

| Función | Qué hace |
|---|---|
| `generate_key()` | Genera una clave aleatoria de 32 bytes codificada en Base64 |
| `encrypt_password(password, key)` | Cifra el texto con la clave Fernet |
| `decrypt_password(encrypted_password, key)` | Descifra el token y retorna el texto original |

---

## 🖥️ Ejemplo de salida

```
Enter the password: MiContraseña123!

--- Encryption Results ---
Encryption key: dGhpcyBpcyBhIHZlcnkgbG9uZyBrZXkgZm9yIGZlcm5ldA==
Encrypted password: gAAAAABmX3k2...  (token cifrado ilegible)
Decrypted password: MiContraseña123!
```

---

## 🧰 Tecnologías

| Librería | Uso |
|---|---|
| `cryptography.fernet` | Implementación del esquema de cifrado Fernet |

### Instalación

```bash
pip install cryptography
```

---

## 🚀 Cómo ejecutarlo

```bash
python desincriptar_fernet.py
```

---

## ⚠️ Consideraciones de seguridad importantes

> **La clave es lo más importante.** Si se pierde, los datos cifrados son irrecuperables.

En un sistema real, la clave Fernet debe:
- 🗄️ Guardarse en un **gestor de secretos** (ej. AWS Secrets Manager, HashiCorp Vault)
- 🚫 **Nunca** hardcodearse en el código fuente
- 🔄 Rotarse periódicamente para minimizar el impacto de una filtración

---

## 📚 Conceptos de seguridad aplicados

- **Cifrado simétrico**: misma clave para cifrar y descifrar (vs. asimétrico como RSA)
- **Cifrado autenticado**: garantiza que el mensaje no fue alterado (AEAD)
- **Gestión de claves (Key Management)**: uno de los mayores desafíos en criptografía aplicada
- **Defense in depth**: proteger datos en tránsito y en reposo con cifrado
