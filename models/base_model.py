#!/usr/bin/python3
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()

class BaseModel:
	id = Column(String(60), primary_key=True, nullable=False)
	created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
	updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)
	def __init__(self, *args, **kwargs):
		if kwargs != {}:
			del kwargs["__class__"]
			for key, value in kwargs.items():
				setattr(self, key, value)
				if "id" not in kwargs:
					self.id = str(uuid.uuid4())
				if "created_at" not in kwargs:
					self.created_at = datetime.utcnow()
				if "updated_at" not in kwargs:
					self.updated_at = datetime.utcnow()
		else:
			self.id = str(uuid.uuid4())
			self.created_at = datetime.utcnow()
			self.updated_at = datetime.utcnow()
	def __str__(self):
		d = self.__dict__.copy()
		d.pop("_sa_instance_state", None)
		return f"[{self.__class__.__name__}] ({self.id}) {d}"
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
