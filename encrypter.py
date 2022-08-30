import hashlib
import uuid

def encrypt(password, *args, **kwargs):
    salt = kwargs.get('salt', uuid.uuid4().hex)
    salt = salt.encode()
    snhpassword = hashlib.sha512(password.encode() + salt).hexdigest()
    return snhpassword
