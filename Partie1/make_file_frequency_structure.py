import re

from Partie1.get_clean_words_in_file import *


def make_file_frequency_structure(key, string):
    # Get all words from string
    words = re.findall(r'\b(.*?)\b', string)
    clean_words = get_clean_words(string)
    return make_dict(clean_words)


def make_dict(clean_words):
    dict = {}
    for word in clean_words:
        if word not in dict and len(word) > 1:
            dict[word] = clean_words.count(word)
    return dict