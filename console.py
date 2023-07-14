#!/usr/bin/python3
"""Defines the HBnB console."""

import cmd
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Command interpreter class for HBNB"""

    prompt = "(hbnb) "
    classes = {
        "BaseModel", "Amenity", "City", "Place", "Review", "State", "User"
    }

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        return True

    def do_create(self, arg):
        """Creates a new instance, saves it to the JSON file, and prints the id"""
        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            objects = models.storage.all()
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            objects = models.storage.all()
            if key in objects:
                objects.pop(key)
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representations of instances"""
        objects = models.storage.all()
        if len(arg) == 0:
            print([str(obj) for obj in objects.values()])
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            print([str(obj)
                  for obj in objects.values() if isinstance(obj, eval(arg))])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            objects = models.storage.all()
            if key not in objects:
                print("** no instance found **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                instance = objects[key]
                attribute = args[2]
                value = args[3].strip("\"'")
                if hasattr(instance, attribute):
                    attr_type = type(getattr(instance, attribute))
                    setattr(instance, attribute, attr_type(value))
                    instance.save()
                else:
                    print("** attribute doesn't exist **")

    def default(self, line):
        """Handle the <class name>.all() command"""
        class_name, _, command = line.partition(".")
        if class_name in self.classes:
            if command == "all()":
                self.do_all(class_name)
            elif command == "count()":
                self.do_count(class_name)
            elif command == "show()":
                self.do_show(class_name)
            else:
                print("** no instance found **")
        else:
            print("*** Unknown syntax: {}".format(line))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
