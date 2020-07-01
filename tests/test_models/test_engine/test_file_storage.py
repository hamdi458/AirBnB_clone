#!/usr/bin/python3
"""unittests for file_storage.py"""
import os
import json
import unittest
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.amenity import Amenity
from models.user import User
from models.review import Review
from models.place import Place
from models.state import State
from models.city import City
from datetime import datetime


class Test_FileStorage(unittest.TestCase):
    """Unittests for filestorage"""

    def test_init(self):
        """test new initialisation"""
        self.assertEqual(type(models.storage), FileStorage)

    def test_arg(self):
        """test args"""
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_path(self):
        """test path"""
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_no_args(self):
        """test no args"""
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_dict(self):
        """test dict"""
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))


class Test_FileStorage_functions(unittest.TestCase):
    """Unittests functions filestorage."""

    @classmethod
    def setUp(self):
        """create"""
        self.objects = FileStorage._FileStorage__objects
        self.file_path = FileStorage._FileStorage__file_path
        self.user = User()
        self.user.save()

    def test_all(self):
        """test aall"""
        self.assertEqual(dict, type(models.storage.all()))

    @classmethod
    def filejson(self):
        """test tearDown"""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("lol", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all_with_arg(self):
        """test all args"""
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_fn_new(self):
        """test meth new"""
        mb = BaseModel()
        rvw = Review()
        usr = User()
        st = State()
        amn = Amenity()
        pl = Place()
        ct = City()
        models.storage.new(mb)
        models.storage.new(rvw)
        models.storage.new(usr)
        models.storage.new(amn)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(ct)
        self.assertIn("BaseModel." + mb.id, models.storage.all().keys())
        self.assertIn(mb, models.storage.all().values())
        self.assertIn("Review." + rvw.id, models.storage.all().keys())
        self.assertIn(rvw, models.storage.all().values())
        self.assertIn("User." + usr.id, models.storage.all().keys())
        self.assertIn(usr, models.storage.all().values())
        self.assertIn("State." + st.id, models.storage.all().keys())
        self.assertIn(st, models.storage.all().values())
        self.assertIn("Amenity." + amn.id, models.storage.all().keys())
        self.assertIn(amn, models.storage.all().values())
        self.assertIn("Place." + pl.id, models.storage.all().keys())
        self.assertIn(pl, models.storage.all().values())
        self.assertIn("City." + ct.id, models.storage.all().keys())
        self.assertIn(ct, models.storage.all().values())

    def test_fn_new_without_args(self):
        """test function new"""
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_fn_new_args_here(self):
        """test function new"""
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_fn_save(self):
        """test methode save"""
        mb = BaseModel()
        rvw = Review()
        usr = User()
        st = State()
        amn = Amenity()
        pl = Place()
        ct = City()
        models.storage.new(mb)
        models.storage.new(rvw)
        models.storage.new(usr)
        models.storage.new(amn)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(ct)
        models.storage.save()
        save_txt = ""
        with open("file.json", "r") as file:
            save_txt = file.read()
            self.assertIn("BaseModel." + mb.id, save_txt)
            self.assertIn("Review." + rvw.id, save_txt)
            self.assertIn("User." + usr.id, save_txt)
            self.assertIn("State." + st.id, save_txt)
            self.assertIn("Amenity." + amn.id, save_txt)
            self.assertIn("Place." + pl.id, save_txt)
            self.assertIn("City." + ct.id, save_txt)

    def test_save_arg(self):
        """test meth save"""
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_fn_reload(self):
        """test meth reload"""
        mb = BaseModel()
        rvw = Review()
        usr = User()
        st = State()
        amn = Amenity()
        pl = Place()
        ct = City()
        models.storage.new(mb)
        models.storage.new(rvw)
        models.storage.new(usr)
        models.storage.new(amn)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(ct)
        models.storage.save()
        models.storage.reload()
        objects = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + mb.id, objects)
        self.assertIn("Review." + rvw.id, objects)
        self.assertIn("User." + usr.id, objects)
        self.assertIn("State." + st.id, objects)
        self.assertIn("Amenity." + amn.id, objects)
        self.assertIn("Place." + pl.id, objects)
        self.assertIn("City." + ct.id, objects)

    def test_reload_args(self):
        """test meth reload"""
        with self.assertRaises(TypeError):
            models.storage.reload(None)

    def test_fn_reload(self):
        """test methode reload"""
        self.assertRaises(FileNotFoundError, models.storage.reload())

if __name__ == "__main__":
    unittest.main()
