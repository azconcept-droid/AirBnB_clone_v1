#!/usr/bin/python3
"""models.__init__ module 
to create a unique FileStorage instance for this application"""

from models.engine.file_storage import FileStorage

storage = FileStorage()

storage.reload()
