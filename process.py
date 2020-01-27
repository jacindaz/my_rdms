import string_parser.parser as str_parse
from db_operations.database import Database

def process(data):
    parsed_result = str_parse.parse_and_validate(data)

    if type(parsed_result) == Exception:
        return parsed_result
    else:
        # TODO: think about who calls
        # the database object?
        operation = parsed_result[0]
        entity = parsed_result[1]
        db_name = parsed_result[2]

        if operation == "create" and entity == "database":
            db = Database(db_name)
            db.create()
