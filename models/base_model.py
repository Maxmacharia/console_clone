#!/usr/bin/python3
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, string

Base = declarative_base()

class BaseModel:
	"""
	creating public instance attribute if the dictonary is not empty set the 	value of the named attribute of the object otherwise created a new objec	t
	"""
	def __init__(self, *args, **kwargs):
		if kwargs != {}:
			del kwargs["__class__"]
			for key, value in kwargs.items():
				setattr(self, key, value)
		else:
			self.id = Column(String(60), default=lambda:str(uuid.uuid4()), unique=True, nullable=False, primary_key=True)
			self.created_at = Column(default=lambda:datetime.utcnow(), nullable=False)
			self.updated_at = Column(default=lambda:datetime.utcnow(), nullable=False)
	def __str__(self):
		return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
	def save(self):
		from models import storage
		storage.new(self)
		storage.save()
		return self.updated_at
	def to_dict(self):
		dictionary = self.__dict__.copy()
		if "_sa_instance_state" in dictionary:
			del dictionary["_sa_instance_state"]
		dictionary["created_at"] = datetime.now().isoformat()
		dictionary["updated_at"] = datetime.now().isoformat()
		dictionary["__class__"] = self.__class__.__name__
		return dictionary
	def delete(self):
		from models import storage
		storage.delete(self)
