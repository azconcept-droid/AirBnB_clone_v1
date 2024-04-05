#!/usr/bin/python3
"""
This module is a command interpreter module.
It contains entry point for command interpreter
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """Command processor"""

    prompt = '(hbnb) '
    file = None

    def do_create(self, arg):
        """Create command to create new instance of BaseModel"""
        if arg:
            print('')
        else:
            print('** class name missing **')

    def do_show(self, kargs):
        """Show command to print the string representation of an instance based on the class name and id"""
        if kargs:
            print('')
        else:
            print('** class name missing **')
    
    def do_destroy(self, kargs):
        """Destroy command to delete an instance based on the class name and id"""
        if kargs:
            print('')
        else:
            print('** class name missing **')

    def do_all(self, kargs):
        """All command to print all string representation of all instances based or not on the class name"""
        if kargs:
            print('')
        else:
            print('all class name')

    def do_update(self, kargs):
        """Update command to update an instance based on the class name and id by adding or updating attribute"""
        if kargs:
            print('')
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