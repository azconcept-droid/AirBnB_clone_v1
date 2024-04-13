#!/usr/bin/python3
"""
This module is a command interpreter module.
It contains entry point for command interpreter
"""

import cmd
from models import storage
from models.base_model import BaseModel


classes = {
    "BaseModel": BaseModel
}

class HBNBCommand(cmd.Cmd):
    """Command processor"""

    prompt = '(hbnb) '
    file = None

    def do_create(self, arg):
        """Create command to create new instance of classes"""
        if arg:
            for name, obj in classes.items():
                if name != arg:
                    print("** class doesn't exist **")
                else:
                    new_obj = obj()
                    new_obj.save()
                    print(new_obj.id)
        else:
            print('** class name missing **')

    def do_show(self, args):
        """Show command to print the string representation of an instance based on the class name and id"""
        if args:
            for name, obj in classes.items():
                if args == name:
                    print("** instance id is missing **")
                else:
                    cls_name = args.split(' ')[0]
                    if cls_name == name:
                        cls_id = args.split(' ')[1]
                        key = "{}.{}".format(cls_name, cls_id)
                        all_objs = storage.all()
                        if key in all_objs.keys():
                            obj = all_objs[key]
                            print(obj)
                        else:
                            print("** no instance found **")
                    else:
                        print("** class doesn't exist **")
        else:
            print('** class name missing **')
    
    def do_destroy(self, args):
        """Destroy command to delete an instance based on the class name and id"""
        if args:
            for name in classes.keys():
                if args == name:
                    print("** instance id is missing **")
                else:
                    cls_name = args.split(' ')[0]
                    if cls_name == name:
                        cls_id = args.split(' ')[1]
                        key = "{}.{}".format(cls_name, cls_id)
                        
                        if key in storage.all().keys():
                            del storage.all()[key]
                            storage.save()
                        else:
                            print("** no instance found **")
                    else:
                        print("** class doesn't exist **")
        else:
            print('** class name missing **')

    def do_all(self, args):
        """All command to print all string representation of all instances based or not on the class name"""
        if args:
            for name in classes.keys():
                if name != args:
                    print("** class doesn't exist **")
                else:
                    print([
                        str(v) for k, v in storage.all().items() 
                        if str(k).split(".")[0] == name
                    ])
        else:
            all_objs = storage.all().values()
            print([str(v) for v in all_objs])

    def do_update(self, args):
        """Update command to update an instance based on the class name and id by adding or updating attribute"""
        if args:
            for name in classes.keys():
                if args == name:
                    print("** instance id is missing **")
                else:
                    # Extract class name
                    cls_name = args.split(' ')[0]
                    if cls_name == name:
                        # Extract class id
                        cls_id = args.split(' ')[1]
                        # Form key from class name and id
                        key = "{}.{}".format(cls_name, cls_id)
                        # Search for the key if it exist
                        if key in storage.all().keys():
                            if args == cls_name + ' ' + cls_id:
                                print("** attribute name missing **")
                            else:
                                # Extract attribute name
                                att_name = args.split(' ')[2]
                                if args == cls_name+' '+cls_id+' '+att_name:
                                    print("** value missing **")
                                else:
                                    # Extract attribute value
                                    att_value = args.split(' ')[3]
                                    dict = [[att_name, att_value]]
                                    for [name, value] in dict:
                                        setattr(storage.all()[key], name, value)
                                    storage.save()
                        else:
                            print("** no instance found **")
                    else:
                        print("** class doesn't exist **")
        else:
            print('** class name missing **')

    def do_quit(self, line):
        """Quit command to exit the program"""
        quit()
        return True

    def emptyline(self):
        """Return bool if line is empty or not"""
        if self == "":
            return True

    def do_EOF(self, line):
        """End of file function"""
        return True

    def postloop(self):
        """Fare well message"""
        print('')

if __name__=="__main__":
    HBNBCommand().cmdloop()