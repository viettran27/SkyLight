from pydantic import BaseModel
from enum import Enum

class Token(BaseModel):
  refresh_token: str

class POSTITON(Enum):
  REQ = "req"
  HOD = "hod"
  ACCT = "acct"
  CA = "ca"
  DIR = "dir"
  CEO = "ceo"
  CFO = "cfo"
  GD = "gd"