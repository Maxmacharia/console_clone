#!/usr/bin/python3

from  models.base_model import BaseModel, Base
from sqlalchemy import Column, String

class User(BaseModel, Base):
	"""class user that inherits from class BaseModel"""
	__tablename__ = 'users'
	email = Column(String(128), nullable=False)
	password = Column(String(128), nullable=False)
	first_name = Column(Stirng(128), nullable=True)
	last_name = Column(Stirng(128), nullable=True)
