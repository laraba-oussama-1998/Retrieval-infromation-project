import json


def get_words_by_document(index):

    reverse_file = json.load(open('reversed_file_by_docs.json', encoding='UTF-8'))
    return [reverse_file[str(index)]]


def get_documents_by_word(word):
    reverse_file = json.load(open('reversed_file_by_words.json', encoding='UTF-8'))
    return [reverse_file[word]]
