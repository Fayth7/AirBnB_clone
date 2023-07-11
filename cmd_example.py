#!/usr/bin/env python3
import cmd
import sys


class PythonInterpreter(cmd.Cmd):
    """ Our console that inherits from the cmd module """
    prompt = "$> "

    if prompt == 'quit':
        sys.exit()

    def do_quit(self, arg):
        """ Quits the program """
        sys.exit()

    def do_exit(self, arg):
        """ Quits the program """
        sys.exit()

    def do_create(self, arg):
        """ Creates a user: Enter <Create> followed by your <name> """
        user = arg
        print(f"Dear {user} welcome to AirBnB")

    def do_update(self, arg):
        """ Updates a user: Enter <Create> followed by your <name> """
        user = arg
        print(f"Dear {user} YOu ae up do date")


if __name__ == "__main__":
    PythonInterpreter().cmdloop()
