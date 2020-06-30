#!/usr/bin/python3
import json
"""class FileStorage"""


class FileStorage():
    """
    serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """objects to the JSON file """
        jsonobj = {}
        for x in self.__objects:
            jsonobj[x] = self.__objects[x].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(jsonobj, f)

    def reload(self):
        """jason to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                loadjason = json.load(f)
            for x in loadjason:
                self.__objects[x] = classes[loadjason[x]["__class__"]](**loadjason[x])
        except:
            pass
