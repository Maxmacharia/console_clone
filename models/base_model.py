#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel:
	"""
	creating public instance attribute if the dictonary is not empty set the 	value of the named attribute of the object otherwise created a new objec	t
	"""
	def __init__(self, *args, **kwargs):
		from models import storage
		if kwargs != {}:
			del kwargs["__class__"]
			for key, value in kwargs.items():
				setattr(self, key, value)
		else:
			self.id = str(uuid.uuid4())
			self.created_at = datetime.now()
			self.updated_at = datetime.now()
			storage.new(self)
	def __str__(self):
		return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
	def save(self):
		from models import storage
		storage.save()
		return self.updated_at
	def to_dict(self):
		self.__dict__["created_at"] = datetime.now().isoformat()
		self.__dict__["updated_at"] = datetime.now().isoformat()
		self.__dict__["__class__"] = self.__class__.__name__
		return self.__dict__
