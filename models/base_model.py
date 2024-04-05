#!/usr/bin/python3
"""Base model module for all classes"""

import uuid
import datetime

class BaseModel():
    """This is base model class"""

    id = str(uuid.uuid4())
    created_at = datetime.now
    updated_at = datetime.now

    def save(self):
        """Updates public instance attribute updated_at with current date time"""
        updated_at = datetime.now
    def to_dict(self):
        """returns a dict containing all keys/values of __dict__ of the instance"""
        
    def __str__():
        """print class name and args"""
        print('[]()<>')