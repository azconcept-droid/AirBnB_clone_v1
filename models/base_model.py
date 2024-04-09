#!/usr/bin/python3
"""Base model module for all classes"""

import uuid
from datetime import datetime

class BaseModel():
    """This is base model class"""

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key is not "__class__":
                    if key in ["created_at", "updated_at"]:
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def save(self):
        """Updates public instance attribute updated_at with current date time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dict containing all keys/values of __dict__ of the instance"""
        instance = self.__dict__.copy()
        instance['__class__'] = self.__class__.__name__
        instance['created_at'] = datetime.isoformat(instance['created_at'])
        instance['updated_at'] = datetime.isoformat(instance['updated_at'])

        return instance
        
    def __str__(self):
        """print object to stdout"""
        cls = self.__class__.__name__
        return "[{}] ({}) {}".format(cls, self.id, self.__dict__)
