# crypto_utils.py
from cryptography.fernet import Fernet

# ВСТАВЬ СЮДА СВОЙ КЛЮЧ из шага 2 (внутри кавычек!)
KEY = b"Aa3_agT-5El_yjg9ByRGO8-gu044y7Hin5i60jwNJ70="

cipher = Fernet(KEY)

def encrypt(text: str) -> bytes:
    """Превращает строку в зашифрованные байты."""
    return cipher.encrypt(text.encode("utf-8"))

def decrypt(token: bytes) -> str:
    """Расшифровывает байты обратно в строку."""
    return cipher.decrypt(token).decode("utf-8")