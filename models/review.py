#!/usr/bin/python3

from models.base_model import BaseModel

class Review(BaseModel):
	"""create review"""
	place_id: str = ""
	user_id: str = ""
	text: str = ""
