#!/usr/bin/python
"""heritage review from base"""
from models.base_class import BaseModel


class State(BaseModel):
    """review"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """initisation new Review"""
        super().__init__(*args, **kwargs)
