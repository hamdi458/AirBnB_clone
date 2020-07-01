#!/usr/bin/python
"""heritage amenity from base"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity"""
    name = ""

    def __init__(self, *args, **kwargs):
        """initialisation new Amenity"""
        super().__init__(*args, **kwargs)
