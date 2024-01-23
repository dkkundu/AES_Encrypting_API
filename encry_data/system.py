# from rest_framework.permissions import AllowAny,
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes #only for AES CBC mode


def encrypt(raw_data, key):
    raw = pad(raw_data.encode(), 16)
    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    return base64.b64encode(cipher.encrypt(raw))


def decrypt(raw_data, key):
    enc = base64.b64decode(raw_data)
    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    return unpad(cipher.decrypt(enc), 16)
