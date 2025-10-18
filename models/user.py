#!/usr/bin/python3
from  models.base_model import BaseModel

class User(BaseModel):
	"""class user that inherits from class BaseModel"""
	email: str = ""
	password: str = ""
	first_name: str = ""
	last_name: str = ""
