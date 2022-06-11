import json
import math
import sys

def get_weighted_reversed_file():
    reversed_file_by_words = json.load(open('reversed_file_by_words.json', encoding='UTF-8'))
    reversed_file_by_docs = json.load(open('reversed_file_by_docs.json', encoding='UTF-8'))
    generic_reversed_file = json.load(open('generic_reverse_file.json', encoding='UTF-8'))
    weighted_reverse_file = {}
    N = len(reversed_file_by_docs)
    for key, value in generic_reversed_file.items():
        key = eval(key)
        word = key[0]
        index = key[1]
        frequency = reversed_file_by_words[word][str(index)]
        Max = max(reversed_file_by_docs[str(index)].values())
        ni = len(reversed_file_by_words[word])
        weight = (frequency / Max) * math.log10((N / ni) + 1)
        weighted_reverse_file[str((word, index))] = weight
    print('length ',len(weighted_reverse_file)," size ",sys.getsizeof(weighted_reverse_file))
    with open('weighted_reversed_file.json', 'w', encoding='UTF-8') as file_writer:
        json.dump(weighted_reverse_file, file_writer, ensure_ascii=False, sort_keys=False)