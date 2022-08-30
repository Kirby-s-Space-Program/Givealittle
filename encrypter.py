import hashlib
import uuid

def encrypt(password, **kwargs):
    salt = kwargs.get('salt', uuid.uuid4().hex) #if no salt given, creates new one
    salt = salt.encode()
    snhpassword = hashlib.sha512(password.encode() + salt).hexdigest()  #salts and hashes password
    return snhpassword
