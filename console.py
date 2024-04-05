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

    def do_quit(self, line):
        """Quit command to exit the program\n"""
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