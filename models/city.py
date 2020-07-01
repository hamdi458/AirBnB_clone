#!/usr/bin/python
"""heritage city from base"""
from models.base_class import BaseModel


class City(BaseModel):
    """City"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """initisation new state"""
        super().__init__(*args, **kwargs)
