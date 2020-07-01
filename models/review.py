#!/usr/bin/python
"""heritage review from base"""
from models.base_model import BaseModel


class Review(BaseModel):
    """review"""
    place_id = ""
    user_id = ""
    text = ""
