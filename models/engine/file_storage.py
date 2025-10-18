#!/usr/bin/python3
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
import json
import os

"""creating class FileStorage"""
class FileStorage:
	"""declaring private class attributes"""
	__file_path = "file.json"
	__objects = {}

	"""developing a function to return the dictionary object"""
	def all(self, cls=None):
		if cls:
			return {k: v for k, v in FileStorage.__objects.items() if isinstance(v, cls)}
		return FileStorage.__objects
	"""developing a function to sets the objects with the key<obj classname.
	id"""
	def new(self, obj):
		key = f"{obj.__class__.__name__}.{obj.id}"
		FileStorage.__objects[key] = obj
	def delete(self, obj=None):
		key = f"{obj.__class__.__name__}.{obj.id}"
		if key in FileStorage.__objects:
			del FileStorage.__objects[key]
	def save(self):
		with open(FileStorage.__file_path, 'w') as json_file:
			json.dump({key: obj.to_dict() for key, obj in FileStorage.__objects.items()}, json_file)
	def reload(self):
		if os.path.exists('file.json'):
			try:
				with open('file.json', 'r') as json_file:
					data = json_file.read()
					if not data:
						return f"The file is empty"
					content = json.loads(data)
					for key, value in content.items():
						name_class = value["__class__"]
						cls = globals()[name_class]
						FileStorage.__objects[key] = cls(**value)
			except (json.JSONDecodeError, FileNotFoundError):
				pass
		else:
			print("The file does not exist")
