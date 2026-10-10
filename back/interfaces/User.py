from dataclasses import dataclass

@dataclass
class User:
  id: int,
  username: str,
  password: str,
  role: 'USER' | 'ADMIN',
  acct_bal: float,
  platform_id: str
  
