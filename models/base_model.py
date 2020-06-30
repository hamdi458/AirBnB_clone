#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
import models
"""
class BaseModel that defines all common attributes/methods for other classes
"""


class BaseModel():
    """class BaseModel that defines all common attributes/methods for
    other classes."""
    def __init__(self, *args, **kwargs):
        """initialise"""
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for x, y in kwargs.items():
                if x == "created_at" or x == "updated_at":
                    self.__dict__[x] = datetime.strptime(y, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[x] = y
        else:
            models.storage.new(self)

    def __str__(self):
        """string"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)
    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()
        models.storage.new(self)

    def to_dict(self):
        """returns a dictionary containing all keys/values"""
        mydict = self.__dict__.copy()
        mydict["created_at"] = self.created_at.isoformat()
        mydict["updated_at"] = self.updated_at.isoformat()
        mydict["__class__"] = self.__class__.__name__
        return mydict
