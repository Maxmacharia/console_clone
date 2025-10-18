#!/usr/bin/python3

from models.base_model import BaseModel

class City(BaseModel):
	"""create cities"""
	state_id: str = ""
	name: str = ""
