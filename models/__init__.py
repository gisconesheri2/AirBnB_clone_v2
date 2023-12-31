#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os

storage_to_use = os.environ['HBNB_TYPE_STORAGE']

# from models.engine.db_storage import DBStorage
# storage = DBStorage()
if storage_to_use == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
