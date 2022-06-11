import json

import numpy as np
from nltk import word_tokenize


class VectorSearch:

    reversed_file_by_words = None
    reversed_file_by_docs = None
    weighted_reversed_file = None
    square_sum = None

    def __init__(self):
        self.reversed_file_by_words = json.load(open('reversed_file_by_words.json', encoding='UTF-8'))
        self.reversed_file_by_docs =  json.load(open('reversed_file_by_docs.json', encoding='UTF-8'))
        self.weighted_reversed_file = json.load(open('weighted_reversed_file.json', encoding='UTF-8'))
        self.square_sum = json.load(open('square_sum.json', encoding='UTF-8'))



    def get_docs_by_vector_model(self, query, method, threshold, size):

        # pairing calculation methods  ['dot', 'dice', 'cos', 'jaccard']
        query_terms = word_tokenize(query)

        # lowercase all words in query
        for i in range(len(query_terms)):
            query_terms[i] = query_terms[i].lower()

        # generate vector space
        vector_space = list(self.reversed_file_by_words.keys())
        query_vector = []

        # save query words
        query_terms_save = []

        # build query's vector
        abort = True
        for word in vector_space:
            if word in query_terms:
                query_vector.append(1)
                query_terms_save.append(word)
                abort = False

        if abort:  # query doesn't match any words of the vector space
            return {}

        results = {}
        for index in self.reversed_file_by_docs.keys():
            doc = []
            proceed = False
            for word in query_terms_save:
                try:
                    doc.append(self.weighted_reversed_file[str((word, int(index)))])
                    proceed = True
                except Exception:
                    doc.append(0)
            result = 0
            if proceed:
                square_vector = self.square_sum[str(index)]
                if method == 'dot':
                    result = np.inner(query_vector, doc)
                elif method == 'dice':
                    result = (2 * np.inner(query_vector, doc)) / (square_vector + sum(np.power(query_vector, 2)))
                elif method == 'cos':
                    result = (np.inner(query_vector, doc)) / (np.sqrt(square_vector * sum(np.power(query_vector, 2))))
                elif method == 'jaccard':
                    result = (np.inner(query_vector, doc)) / (
                            square_vector + sum(np.power(query_vector, 2)) - np.inner(query_vector, doc))
            if result > threshold:
                results[index] = result

        if size is not None:
            return sorted(results.items(), key=lambda x: (x[1], x[0]), reverse=True)[:size]
        else:
            return sorted(results.items(), key=lambda x: (x[1], x[0]), reverse=True)


