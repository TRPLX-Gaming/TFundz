import os 
from dotenv import load_dotenv 

load_dotenv()

class Secrets:
  def __init__(self):
    # INIT ALL env vars 
    self.HASH_SALT = os.getenv('HASH_SALT')
    self.ITERATIONS = os.getenv('ITERATIONS')
    self.KEY_LENGTH = os.getenv('KEY_LENGTH')
    self.USER_ID_SALT = os.getenv('USER_ID_SALT')
    self.USER_ID_LEN = os.getenv('USER_ID_LEN')
    self.USER_ID_ITR = os.getenv('USER_ID_ITR')
    self.DATABASE_URL = os.getenv('DATABASE_URL')
    
# end of class 

secret = Secrets()
#print(os.urandom(4).hex())