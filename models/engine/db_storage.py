#!/usr/bin/python3
import os
from sqlalchemy import create_engine
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy.orm import scoped_session, sessionmaker

class DBStorage:
	__engine = None
	__session = None
	def __init__(self):
		db_user = os.getenv("HBNB_MYSQL_USER")
		db_pass = os.getenv("HBNB_MYSQL_PWD")
		db_host = os.getenv("HBNB_MYSQL_HOST")
		db_name = os.getenv("HBNB_MYSQL_DB")
		env = os.getenv("HBNB_ENV")
		
		db_url = f"mysql+mysqldb://{db_user}:{db_pass}@{db_host}/{db_name}"
		self.__engine = create_engine(db_url, pool_pre_ping=True)

		if env == "test":
			Base.metadata.drop_all(self.__engine)
	def all(self, cls=None):
		obj_dict = {}
		classes = [State, City, User]
		if cls:
			if isinstance(cls, str):
				cls = eval(cls)
			query_result = self.__session.query(cls).all()
			for obj in query_result:
				key = f"{obj.__class__.__name__}.{obj.id}"
				obj_dict[key] = obj
		else:
			for c in classes:
				query_result = self.__session.query(c).all()
				for obj in query_result:
					key = f"{obj.__class__.__name__}.{obj.id}"
					obj_dict[key] = obj
		return obj_dict

	def new(self, obj):

		if obj:
			print("Adding object:", obj)
			self.__session.add(obj)
	def save(self):
		print("Commiting changes to DB....")
		self.__session.commit()
	def delete(self, obj=None):
		if obj:
			self.__session.delete(obj)
	def reload(self):
		Base.metadata.create_all(self.__engine)
		session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
		Session = scoped_session(session_factory)
		self.__session = Session()
