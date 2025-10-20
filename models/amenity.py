#!/usr/bin/python3

from models.base_model import BaseModel, Base
from models.amenity import Amenity

class Amenity(BaseModel, Base):
	"""creates amenity"""
	__tablename__ = 'amenities'
	name = Column(String(128), nullable=False)

	place_amenities = relationship("Place", secondary="place_amenity", viewonly=True)
