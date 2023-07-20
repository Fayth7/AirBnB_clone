#!/usr/bin/python3
"""Defines the HBnB console."""

import cmd
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json
from shlex import split


class HBNBCommand(cmd.Cmd):
    """Command interpreter class for HBNB"""

    prompt = "(hbnb) "
    classes = {
        "BaseModel", "Amenity", "City", "Place", "Review", "State", "User"
    }

    def parseline(self, line):
        """Override the default parseline() method to handle <class name>.all() command"""
        line = line.strip()
        if line.startswith("."):
            line = line[1:]
        if line.startswith("<") and line.endswith(">"):
            cmd, arg = line[1:-1], ""
        else:
            cmd, _, arg = line.partition(" ")
        return cmd, arg, line

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    # def do_emptyline(self):
    #     """Do nothing when an empty line is entered"""
    #     return True

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
        from models import storage
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            objects = storage.all()
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        from models import storage
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            objects = storage.all()
            if key in objects:
                objects.pop(key)
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representations of instances"""
        from models import storage
        arg_list = split(arg)
        objects = storage.all().values()
        if not arg_list:
            # In case no arguments are passed
            print([str(obj) for obj in objects])
        else:
            if arg_list[0] not in self.classes:
                # In Case a wrong class is passed
                print("** class doesn't exist **")
            else:
                # In case a right class is passed
                print([str(obj) for obj in objects
                       if arg_list[0] in str(obj)])

        # from models import storage
        # args = arg.split()
        # if len(args) == 0:
        #     objects = storage.all()
        #     print([str(obj) for obj in objects.values()])
        # elif args[0] not in self.classes:
        #     print("** class doesn't exist **")
        # else:
        #     # print([str(obj)
        #     # for obj in objects.values() if isinstance(obj, eval(arg))])
        #     class_name = args[0]
        #     objects = storage.all(class_name)
        #     print([str(obj) for obj in objects])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        from models import storage
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            objects = storage.all()
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
            elif command.endswith("\")"):
                func, _, clas_id = command.partition("(\"")
                id = clas_id[:-2]
                new_command = f"{class_name} {id}"
                if func == "show":
                    self.do_show(new_command)
                elif func == "destroy":
                    self.do_destroy(new_command)
            elif command.startswith("update"):
                # User.update("4726cdcc-50e2-48b0-aebc-9fd403a36d8e", "first_name", "John")
                # update User 4726cdcc-50e2-48b0-aebc-9fd403a36d8e first_name "Emma"
                func, _, others = command.partition("(")
                args = others.split(", ")
                id = args[0].strip("\"")
                name = args[1]
                value = args[2].strip(")")
                stripped_command = f"{class_name} {id} {name} {value}"
                self.do_update_id(stripped_command)
            else:
                print("** no instance found **")
        else:
            print("*** Unknown syntax: {}".format(line))

    # def do_help(self, arg):
    #     """Display help information"""
    #     if arg == "":
    #         print("Documented commands (type help <topic>):")
    #         print("========================================")
    #         print("EOF  all  create  destroy  help  quit  show  update")
    #     else:
    #         super().do_help(arg)

    def do_count(self, arg):
        """Counts the number of instances of a class"""
        from models import storage
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            class_name = args[0]
            objects = storage.all()
            count = sum(1 for obj in objects.values()
                        if type(obj).__name__ == class_name)
            print(count)

    def do_show_id(self, arg):
        """Show an instance based on its ID"""
        from models import storage
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance ID missing **")
        else:
            class_name = args[0]
            instance_id = args[1].strip("\"'")
            objects = storage.all()
            key = "{}.{}".format(class_name, instance_id)
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy_id(self, arg):
        """Destroy an instance based on its ID"""
        from models import storage
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance ID missing **")
        else:
            class_name = args[0]
            instance_id = args[1].strip("\"'")
            objects = storage.all()
            key = "{}.{}".format(class_name, instance_id)
            if key in objects:
                objects.pop(key)
                storage.save()
            else:
                print("** no instance found **")

    def do_update_id(self, arg):
        """Update an instance based on its ID"""
        from models import storage
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance ID missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            class_name = args[0]
            instance_id = args[1].strip("\"'")
            attribute_name = args[2]
            attribute_value = args[3].strip("\"'")
            objects = storage.all()
            key = "{}.{}".format(class_name, instance_id)
            if key in objects:
                instance = objects[key]
                if hasattr(instance, attribute_name):
                    attr_type = type(getattr(instance, attribute_name))
                    setattr(instance, attribute_name,
                            attr_type(attribute_value))
                    instance.save()
                else:
                    print("** attribute doesn't exist **")
            else:
                print("** no instance found **")

    def do_update_dict(self, arg):
        """Update an instance based on its ID with a dictionary representation"""
        from models import storage
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance ID missing **")
        elif len(args) == 2:
            print("** dictionary representation missing **")
        else:
            class_name = args[0]
            instance_id = args[1].strip("\"'")
            dictionary = ' '.join(args[2:]).replace("'", "\"")
            try:
                attrs = json.loads(dictionary)
                objects = storage.all()
                key = "{}.{}".format(class_name, instance_id)
                if key in objects:
                    instance = objects[key]
                    for attr, value in attrs.items():
                        if hasattr(instance, attr):
                            attr_type = type(getattr(instance, attr))
                            setattr(instance, attr, attr_type(value))
                            instance.save()
                        else:
                            print("** attribute doesn't exist **")
                else:
                    print("** no instance found **")
            except ValueError:
                print("** invalid dictionary representation **")

    def do_count(self, arg):
        """Counts the number of instances of a class"""
        from models import storage
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            class_name = args[0]
            objects = storage.all()
            count = sum(1 for obj in objects.values()
                        if type(obj).__name__ == class_name)
            print(count)

    def do_show_id(self, arg):
        """Show an instance based on its ID"""
        from models import storage
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance ID missing **")
        else:
            class_name = args[0]
            instance_id = args[1].strip("\"'")
            objects = storage.all()
            key = "{}.{}".format(class_name, instance_id)
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")


if __name__ == '__main__':
    from models import storage
    storage.reload()
    HBNBCommand().cmdloop()
