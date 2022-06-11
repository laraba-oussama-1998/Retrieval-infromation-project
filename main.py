from GUI.start_gui import *
from Partie1.get_file_meta import *
from Partie1.make_reversed_file import *
from Partie3.get_weighted_reversed_file import *
import time
import json
import sys
# from Partie4.get_docs_by_vector_model import get_docs_by_vector_model


# --------------------------------------------------> G U I <-----------------------------------------------------------

start_gui()


# -------------------------------------------------> P A R T 1 <--------------------------------------------------------
# Retrieve from cacm.all document identification, title, summary, authors (those are called file meta data)
#indexation
#print('Generating reversed files, please wait ...')
#start = time.time()
#make_reversed_files()
#print('reversed files generated and extracted as .json for future uses. Time : '+str(time.time()-start)+' sec')

# Access function
# # function 1
# start_time = time.time()
# index = 1000
# results = get_words_by_document(index)
# print("Results : "+str(results))

# # function 2
# start_time = time.time()
# word = 'preliminary'
# results = get_documents_by_word(word)


# -------------------------------------------------> P A R T 2 <--------------------------------------------------------
# Construct boolean model
# print('Generating Boolean model, please wait ...')
# start = time.time()
# get_boolean_structure()
# print('Boolean model generated. Time : '+str(time.time()-start)+' sec')

# query = 'artificial and intelligence'
# print('searching query results with boolean model, please wait ...')
# start = time.time()
# results = get_docs_by_boolean_model(query)
# print('process complete. results : '+str(results))
# print('Time '+ str(time.time() - start))

# -------------------------------------------------> P A R T 3 <--------------------------------------------------------
#print('Generating weighted reversed file, please wait ...')
#start = time.time()
#get_weighted_reversed_file()
#print('process complete. Time : '+str((time.time() - start)) + ' sec')

# -------------------------------------------------> P A R T 4 <--------------------------------------------------------
# construct vector model
# start = time.time()
# print('Generating vector model, please wait ...')
# construct_vector_model()
# print('Task completed. Time : '+str(time.time()-start))

# Test query with vector model
# words that aren't in our vector space (the word rfgjhrfgjkergh for instance) will not contribute in pairing process,
# thus, those words will be ignored (inconvenience of vector model)

# query = 'artificial intelligence'
#
# print('searching for docs for query "'+query+'", please wait ...')
# start = time.time()
# result = get_docs_by_vector_model(query, method='dice')
# print("search done. Time : "+ str(time.time() - start) + " sec")
#
# if len(result) > 0:
#     print("Pertinent documents are :")
#     print('_________________________________')
#     for index, weight in result:
#         print("Document "+str(index))
# else:
#     print("No pertinent document found")

# Generate square sum
# print('Generating square sums, please wait ...')
# start = time.time()
# reversed_file_by_docs = json.load(open('reversed_file_by_docs.json', encoding='UTF-8'))
# weighted_reversed_file = json.load(open('weighted_reversed_file.json', encoding='UTF-8'))
# reversed_file_by_words = json.load(open('reversed_file_by_words.json', encoding='UTF-8'))
# vector_space = list(reversed_file_by_words.keys())
# square_sum = {}
# for index in reversed_file_by_docs.keys():
#     doc = []
#     for word in vector_space:
#         try:
#             doc.append(weighted_reversed_file[str((word, int(index)))])
#             proceed = True
#         except Exception:
#             doc.append(0)
#     square_sum[index] = sum(np.power(doc, 2))
#
#
# with open('square_sum.json', 'w', encoding='UTF-8') as file_writer:
#     json.dump(square_sum, file_writer, ensure_ascii=False, sort_keys=False)
# print('Process complete. Time : '+str(time.time()-start)+' sec')

# -------------------------------------------------> P A R T 5 <--------------------------------------------------------

# Extract useful data to .json file
# lines = open("CACM/query.text").readlines()
# query_meta = {}
# queries_meta = {}
#
# for i in range(0, len(lines)):
#
#     # Detect index of a query
#     match = re.match(r'\.I ([0-9]+)', lines[i])
#     if match:
#         if query_meta.__len__() != 0:
#             query_meta["docs"] = list()
#             queries_meta[query_meta['index']] = query_meta
#             query_meta = {}
#         # Detect starting of a document
#         query_meta['index'] = int(match.group(1))
#
#     # Detect query text
#     query = ''
#     if re.match(r'\.W', lines[i]):
#         i = i + 1
#         for j in range(i, len(lines)):
#             if re.match(r'\.[A-Z]', lines[j]):
#                 break
#             query = query + ' ' + lines[j].replace('\n', '')
#         query_meta['query'] = query.lstrip()
#
#     # Detect authors
#     authors = []
#     if re.match(r'\.A', lines[i]):
#         i = i + 1
#         for j in range(i, len(lines)):
#             if re.match(r'\.[A-Z]', lines[j]):
#                 break
#             authors.append(lines[j].replace('\n', ''))
#         query_meta['authors'] = authors
#
#     if i == len(lines) - 1:
#         query_meta["docs"] = list()
#         queries_meta[query_meta['index']] = query_meta
#
# # Get pertinent documents for each query
#
# file = open("CACM/qrels.text")
#
# for line in file:
#     pattern = re.findall(r"[0-9]+", line)
#     queries_meta[int(pattern[0])]['docs'].append(pattern[1])
#
# with open('query_meta.json', 'w', encoding='UTF-8') as file_writer:
#     json.dump(queries_meta, file_writer, ensure_ascii=False, sort_keys=False)












