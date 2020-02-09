import string_parser.parser as str_parse
from db_operations.database import Database

def process(data):
    parsed_result = str_parse.parse_and_validate(data)

    if type(parsed_result) == Exception:
        return parsed_result
    else:
        word_len = len(parsed_result)

        if word_len == 3:
            # TODO: think about who calls
            # the database object?
            operation = parsed_result[0]
            entity = parsed_result[1]
            db_name = parsed_result[2]

            if operation == "create" and entity == "database":
                db = Database(db_name)
                db.create()
        elif word_len == 2:
            operation = parsed_result[0]
            name = parsed_result[1]

            if operation == "\\c":
                # connect to a database
                pass
