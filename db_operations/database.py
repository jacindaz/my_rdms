import os
import logging

class Database:
    def __init__(self, name, schema="public"):
        self.name = name
        self.schema = schema

    def create(self):
        """
        If database already exists: error
        If not: create new directory in public
        """

        database_exists = os.path.isdir(f"data_files/{self.schema}/{self.name}")
        if database_exists:
            logging.error("database already exists")
            exception = Exception()
            exception.msg = "database already exists"
            return exception
        else:
            os.mkdir(f"data_files/{self.schema}/{self.name}")
            logging.info("Created database!")
