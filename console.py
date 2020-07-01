#!/usr/bin/python3
""" HBNH console """

import cmd


class HBNBCommand(cmd.Cmd):
    """ HBNH console """
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """ to Exit the console"""
        return True

    def emptyline(self):
        """ emptyline method """
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
