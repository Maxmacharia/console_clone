#!/usr/bin/python3

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float
from typing import List

class Place(BaseModel):
	"""creating place"""
	__tablename__ = 'palces'
	city_id = Column(String(60), nullable=False, ForeignKey('cities.id'))
	user_id = Column(String(60), nullable=False, ForeignKey('users.id'))
	name = Column(String(128), nullable=False)
	description = Column(String(128), nullable=True)
	number_rooms = Column(Integer, nullable=False, default=0)
	number_bathrooms = Column(Integer, nullable=False, default=0)
	max_guest = Column(Integer, nullable=False, default=0)
	price_by_night = Column(Integer, nullable=False, default=0)
	latitude = Column(Float, nullable=True)
	longtitude = Column(Float, nullable=True)
	#amenity_ids: List[str] = []
