from pydantic import BaseModel
from enum import Enum

class Token(BaseModel):
  refresh_token: str

