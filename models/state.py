#!/usr/bin/python
"""heritage state from base"""
from models.base_model import BaseModel


class State(BaseModel):
    """state"""
    name = ""

    def __init__(self, *args, **kwargs):
        """initialisation new State"""
        super().__init__(*args, **kwargs)
