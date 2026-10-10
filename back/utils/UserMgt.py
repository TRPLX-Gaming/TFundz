from pathlib import Path 
import json
import utils.id as uid

# note: every instance method must have the 'self' parameter to make it an instance else it turns to a static method

class UserMgt:
  # ommited constructor
  
  CURRENT_DIR = Path(__file__).resolve()
  ROOT_DIR = CURRENT_DIR.parent.parent
  DATABASE = ROOT_DIR / 'db/db.json'
  
  # adding user to db
  def add_user(
    self,
    username,
    password,
    role,
    nickname
  ):
    data = self.get_users()
    
    user = {
      'id': uid.assign_ID(),
      'username': username,
      'password':password,
      'role': role,
      'nickname': nickname,
      'acct_bal': 0,
      'platform_id': 'Unavailable'
    }
    data["users"].append(user)
    with open(UserMgt.DATABASE,'w',encoding='utf-8') as file:
      json.dump(data,file,indent=4,sort_keys=True)
    return user
  
  # modify a users attrs
  def modify_user(self,user_id,attribute,updated_value):
    pass
  
  # remove a user
  def delete_user(self,user_id):
    pass 
  
  def get_users(self):
    with open(UserMgt.DATABASE, 'r', encoding='utf-8') as file:
      data = json.load(file)
      
    return data['users']
    
    
user_handler = UserMgt()