#!/usr/bin/python3

import os
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review

storage_type = os.getenv("HBNB_TYPE_STORAGE")
if storage_type == "db":
	storage = DBStorage()
else:
	storage = FileStorage()

storage.reload()
print("Storage type loaded:", type(storage).__name__)
