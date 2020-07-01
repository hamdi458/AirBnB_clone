#!/usr/bin/python3
""" HBNH console """


import cmd
import shlex
import models
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ HBNH console """
    prompt = '(hbnb) '
    classes = {"Place": Place, "Amenity": Amenity, "BaseModel": BaseModel,
               "Review": Review, "State": State, "User": User, "City": City}

    def do_EOF(self, arg):
        """ to Exit the console"""
        return True

    def emptyline(self):
        """ emptyline method """
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
        if args[0] in HBNBCommand.classes:
            i = HBNBCommand.classes[args[0]]()
        else:
            print("** class doesn't exist **")
        print(i.id)
        i.save()

    def do_show(self, line):
        """ Prints the string representation of an
        instance based on the class name and id """
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in HBNBCommand.classes:
            if len(args) == 1:
                print("** instance id missing **")
            else:
                models.storage.reload()
                getall = models.storage.all()
                if args[0] + '.' + args[1] in list(getall.keys()):
                    print(getall[args[0] + '.' + args[1]])
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        """ Deletes an instance based on the class
        name and id
        """
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in HBNBCommand.classes:
            if len(args) == 1:
                print("** instance id missing **")
            else:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_all(self, line):
        """ Prints all string representation
        of all instances based or not on the class name.
        """
        obj = []
        args = shlex.split(line)
        if len(args) == 0 or len(args) == 1 and args[0] in HBNBCommand.classes:
            for x in list(models.storage.all().keys()):
                if line == "":
                    obj.append(str(models.storage.all()[x]))
                else:
                    if args[0] in x:
                        obj.append(str(models.storage.all()[x]))
            print(obj)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance based
        on the class name and id
        by adding or updating attribute
        """
        get_all = models.storage.all()
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in HBNBCommand.classes:
            if len(line) == 1:
                print("** instance id missing **")
            else:
                x = args[0] + "." + args[1]
                if x not in get_all:
                    print("** no instance found **")
                else:
                    if len(args) == 2:
                        print("** attribute name missing **")
                    elif len(args) == 3:
                        print("** value missing **")
                    else:
                        setattr(get_all[x], args[2], args[3])
                        models.storage.all()[x].save()
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
