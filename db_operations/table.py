import os
import logging

class Table:
    def __init__(self, name, schema="public"):
        self.name = name
        self.schema = schema

    def create(self):
        """
        """
        schema_exists = os.path.isdir(f"data_files/{self.schema}")
        if schema_exists:
            table_exists = os.path.isdir(f"data_files/{self.schema}/{self.name}")
            if table_exists:
                logging.error("database already exists")
                exception = Exception()
                exception.msg = "database already exists"
                return exception
            else:
                os.mkdir(f"data_files/{self.schema}/{self.name}")
                logging.info("Created database!")
        else:
            logging.error(f"schema {self.schema} does not exist")
            exception = Exception()
            exception.msg = f"schema {self.schema} does not exist"
            return exception
