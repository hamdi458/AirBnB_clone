#!/usr/bin/python
"""heritage amenity from base"""
from models.base_model import BaseModel


class State(BaseModel):
    """Amenity"""
    name = ""

    def __init__(self, *args, **kwargs):
        """initisation new amenity"""
        super().__init__(*args, **kwargs)
