#!/usr/bin/python3
"""File storage module"""

import json
import os

class FileStorage:
    """This class serializes instances to a JSON file 
    and deserializes JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns all stored objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        obj_dict = {}

        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()

        # Convert obj_dict to string and write it in file.json
        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                from models.base_model import BaseModel

                class_name = {
                    "BaseModel": BaseModel
                }

                for key, value in json.load(file).items():
                    # Extract class name from key
                    ext_cls_name = key.split('.')[0]
                    # Recreate the object from json
                    self.new(class_name[ext_cls_name](**value))
