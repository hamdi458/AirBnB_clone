#!/usr/bin/python
"""heritage city from base"""
from models.base_model import BaseModel


class City(BaseModel):
    """City"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """initialisation new City"""
        super().__init__(*args, **kwargs)
