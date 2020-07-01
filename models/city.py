#!/usr/bin/python
"""heritage city from base"""
from models.base_model import BaseModel


class City(BaseModel):
    """City"""
    state_id = ""
    name = ""
