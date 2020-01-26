import string_parser.parser as str_parse
from db_operations.database import Database

def process(data):
    parsed_result = str_parse.parse_and_validate(data)

    if type(parsed_result) == Exception:
        return parsed_result.msg
    else:
        # TODO: think about who calls
        # the database object?
        operation = parsed_result[0]
        entity = parsed_result[1]
        db_name = parsed_result[2]
        if operation == "create" and entity == "database":
            name_and_schema = db_name.split(".")
            if len(name_and_schema) == 2:
                db_name = name_and_schema[0]
                schema_name = name_and_schema[1]
                db = Database(db_name, schema=schema_name)
            else:
                db = Database(db_name)

            db.create()

    return "success!"
