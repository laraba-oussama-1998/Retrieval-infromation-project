import json

from nltk import word_tokenize


def get_docs_by_boolean_model(query):
    boolean_model = json.load(open('reversed_file_by_docs.json', 'r', encoding='UTF-8'))
    query_words = word_tokenize(query)
    docs = []
    for index, words in boolean_model.items():
        query_doc = word_tokenize(query)
        for word in query_words:
            if word not in ['and', 'or', 'not', '(', ')']:
                if word in words.keys():
                    query_doc[query_doc.index(word)] = '1'
                else:
                    query_doc[query_doc.index(word)] = '0'
        # Evaluate the boolean expression (each word is replaced by 0 or 1 depending on it existence on the document
        try:
            if eval(' '.join(query_doc)) == 1:
                docs.append(index)
        except Exception:
            return -1
    return docs