import json


def construct_vector_model():
    reversed_file_by_docs = json.load(open('reversed_file_by_docs.json', encoding='UTF-8'))
    reversed_file_by_words = json.load(open('reversed_file_by_words.json', encoding='UTF-8'))
    vector_space = list(reversed_file_by_words.keys())
    weighted_reversed_file = json.load(open('weighted_reversed_file.json', encoding='UTF-8'))
    vector_model = {}
    for index in reversed_file_by_docs:
        vector = []
        for word in vector_space:
            key = (word, int(index))
            if (index in reversed_file_by_words[word]):
                vector.append(weighted_reversed_file[str(key)])
            else:
                vector.append(0)
        vector_model[index] = vector

    with open('vector_model.json', 'w', encoding='UTF-8') as file_writer:
        json.dump(vector_model, file_writer, ensure_ascii=False, sort_keys=False)


