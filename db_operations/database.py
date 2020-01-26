class Database:
    def __init__(self, name, schema="public"):
        self.name = name
        self.schema = schema

    def create(self):
        """
        If database already exists:
          -> error

        If not:
          -> if specifies schema, and schema
             does not exist, error
          -> create new directory in public
        """

        # -> check if schema exists
        # -> check if db exists
        return "does not do anything yet!"
