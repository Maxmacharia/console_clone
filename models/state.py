#!/usr/bin/python3

from models.base_model import BaseModel, Base
from models import City
from sqlalchmey import Column, String
from sqlalchemy import relationship

class State(BaseModel):
	"""class state create states"""
	__table__ = 'states'
	name = Column(String(128), nullable=False)

	cities = relationship(
		"City",
		backref="state",
		cascade="all, delete, delete-orphan"
	)
