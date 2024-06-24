#!/usr/bin/python3
"""
Initialize the models package
"""

from os import getenv

# DBStorage or FileStorage?
storage_type = getenv("HBNB_TYPE_STORAGE")

if storage_type == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
