import os 
import base64
import zlib
import hashlib
from utils.Secrets import secret

class Crypto:
  def __init__(self):
    self.HASH_SALT = bytes.fromhex(secret.HASH_SALT)
    self.ITERATIONS = int(secret.ITERATIONS)
    self.KEY_LENGTH = int(secret.KEY_LENGTH)
    self.USER_ID_SALT = bytes.fromhex(secret.USER_ID_SALT)
    self.USER_ID_ITR = int(secret.USER_ID_ITR)
    self.USER_ID_LEN = int(secret.USER_ID_LEN)
  
  def encrypt_token(token: dict):
    pass
  
  def decrypt_token(encrypted_token):
    pass
  
  def hash_token():
    pass
  
  def encrypt(self,value: str) -> str:
    raw_bytes = value.encode('utf-8')
    compressed_data = zlib.compress(raw_bytes)
    return base64.urlsafe_b64encode(compressed_data).decode('utf-8')
    
  def decrypt(self,encrypted_val: str) -> str:
    try:
      compressed_data = base64.urlsafe_b64decode(encrypted_val.encode('utf-8'))
      
      raw_bytes = zlib.decompress(compressed_data)
      return raw_bytes.decode('utf-8') 
    except Exception:
      raise ValueError('invalid or corrupted data')
  
  def compare_token_hash():
    pass
  
  def hash_password(self,password: str) -> str:
    password_bytes = password.encode('utf-8')
    
    hashed_password = hashlib.pbkdf2_hmac(
      hash_name='sha256',
      password=password_bytes,
      salt=self.HASH_SALT,
      iterations=self.ITERATIONS,
      dklen=self.KEY_LENGTH
    )
    return hashed_password.hex()
    
  def create_ID(self) -> str:
    ran_str = str(os.urandom(4).hex())
    ran_bytes = ran_str.encode('utf-8')
    
    generated_ID = hashlib.pbkdf2_hmac(
      hash_name='sha256',
      password=ran_bytes,
      salt=self.USER_ID_SALT,
      iterations=self.USER_ID_ITR,
      dklen=self.USER_ID_LEN
    )
    
    return generated_ID.hex()
    
  

crypto = Crypto()

# speculative feature: if file dbms is used, encrypt file for extra security