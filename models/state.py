#!/usr/bin/python
"""heritage state from base"""
from models.base_class import BaseModel


class State(BaseModel):
    """state"""
    name = ""

    def __init__(self, *args, **kwargs):
        """initisation new state"""
        super().__init__(*args, **kwargs)
