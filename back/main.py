from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text 
from utils.UserMgt import user_handler
from utils.Crypto import crypto
from utils.Secrets import secret
import ssl

app = Flask(__name__)
CORS(app)

# db stuff
ssl_context = ssl.create_default_context()
app.config['SQLALCHEMY_DATABASE_URI'] = secret.DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
  'connect_args': {
    'ssl_context': ssl_context
  }
}

#init db 
db = SQLAlchemy(app)

# connect to db 
def connecf_db():
  try:
    with app.app_context():
      db.session.execute(text('SELECT 1'))
      print('db connected!')
  except Exception as e:
    print(f'Error while connecting to db. reason: {e}')

# schema & model def 
class User(db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(100), unique=True, nullable=False)
  email = db.Column(db.String(140), unique=True, nullable=False)
  
  def to_dict(self):
    return {
      'id':self.id,
      'username': self.username,
      'email': self.email
    }
    
# server made custom cmd 
# @app.cli.command('init-db')
# def init_db():
#   db.create_all()
#   print('Database tables ready!')

@app.route('/', methods=['GET'])
def get():
  return jsonify({"message": "server running"})
  
# db 
@app.route('/users/data', methods=['GET'])
def fetch_users():
  users = User.query.all()
  all_users = []
  for u in users:
    all_users.append(u.to_dict())
    
  return all_users,200
    
@app.route('/users/data/local', methods=['GET'])
def get_users():
  return jsonify(user_handler.get_users())
  
@app.route('/users/signup', methods=['POST'])
def new_user():
  data = request.get_json(silent=True)
  if not data:
     return jsonify({"message":"incomplete or invalid data sent"}),400
     
  username = data.get('username')
  role = data.get('role','user') # defaults to user 
  nickname = data.get('nickname','noob')
  
  if not username:
    return jsonify({"message":"username is required"}), 400 
    
  result = user_handler.add_user(username,role,nickname)
  return jsonify({"message":"user created!", "user":result}), 201

# testing crypto 
@app.route('/test/crypto',methods=['POST'])
def crypt():
  data = request.get_json(silent=True) or {}
  
  if not data:
    return jsonify({"message":"invalid or missing payload"}), 400
  
  mode = data.get('mode')
  payload = data.get('payload')
  
  if not mode:
    return jsonify({'message':'mode not defined!'})
    
  if not payload:
    return jsonify({'message':'missing value to perform action on'})
    
  if mode == 'encrypt':
    pass
  elif mode == 'decrypt':
    pass
  elif mode == 'hash':
    pass
  else:
    return jsonify({'message':'undefined or missing mode'})



if __name__ == '__main__':
  connecf_db()
  app.run(host='0.0.0.0', port=5000, debug=True)
