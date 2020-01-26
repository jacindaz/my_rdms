import ipdb

# THINK ABOUT:
#   -> this eventually will probably be a tree of
#      keywords and valid operations with those keywords
#   -> children will help with validating ordering
#   -> ex: "database jacinda create" is invalid
KEYWORDS = {
    "create": set(["database", "table"]),
    "drop": set(["database", "table"]),
}

def parse_and_validate(mystr):
    """
    """

    # Postgres lowercases all table/database names
    mystr = mystr.lower()
    words = mystr.split(" ")
    num_words = len(words)

    if num_words >= 1:
        operation = words[0]
    if num_words >= 2:
        entity = words[1]

    if operation in KEYWORDS and entity in KEYWORDS[operation]:
        if operation == "create" and entity == "database":
            if num_words == 3:
                return words
            else:
                excpt = Exception()
                excpt.msg = "Too many inputs for create database."
                return excpt
