import json

from Partie1.get_clean_words_in_file import get_clean_words
from Partie1.stringify_file import stringify_file


def get_boolean_structure():
    meta = json.load(open('meta.json', encoding='UTF-8'))
    struct = {}
    for key in meta.keys():
        # Step 1 : convert file meta data into a string to easily extract useful words
        file_string = stringify_file(meta[key])
        # Step 2 : get document useful words in a list
        clean_words = get_clean_words(file_string)
        struct[key] = clean_words
    with open('boolean.json', 'w', encoding='UTF-8') as file_writer:
        json.dump(struct, file_writer, ensure_ascii=False, sort_keys=False)
    return struct

