import json
import nltk
from nltk.corpus import stopwords
import re
from nltk.tokenize import word_tokenize
import math
import time
import sys

from Partie1.make_file_frequency_structure import *
from Partie1.stringify_file import stringify_file



stp_word=stopwords.words('english')
stp_word.append(",")
stp_word.append(":")
stp_word.append(".")

def make_reversed_files():
    cacm = open("CACM/cacm.all","r")
    start= time.time()
    document_numbers=[]
    document_words=[]
    text=""
    copy=False
    test=[]
    for line in cacm:
    #print("line",line)
        test.append(re.findall("\w+",line))
        if re.findall(".I[\s]+[0-9]+",line):
           document_numbers.append(line.split()[1])
           document_words.append(text.split())
           text=""
    #print(line[0:2])
        if line[0:2] in [".T",".W",".A"]:
           copy=True
        elif line[0:2] in [".B",".N",".X"]:
           copy=False
        if copy and line[0:2] not in [".T",".W",".A"]:
           text+=""+line.lower()
    document_words.append(text.split())
# remove the first document which is [] its important dont remove it!!  
    document_words.pop(0)
#print(document_words)
#print(text.split())
#print(document_numbers) 
#print(document_words[0])
    i=0
    dictionnaire={}

    dictionnaire_mot=nltk.defaultdict(int)

    for document in document_words:
       for word in document:
          list_word=re.findall(r"\b\w+\b",word)
          if len(list_word)>=2:
         
             if len(list_word[0])> 2 and list_word[0] not in stp_word:
                dictionnaire_mot[list_word[0]]+=1
         
             try:
                if len(list_word[2])> 2 and list_word[2] not in stp_word:
                    dictionnaire_mot[list_word[2]]+=1
             #print("**********",word)
                if len(list_word[1])> 2 and list_word[1] not in stp_word:
                    dictionnaire_mot[list_word[1]]+=1
             
             
             except:
           
                  if len(list_word[1])> 2 and list_word[1] not in stp_word:
                     dictionnaire_mot[list_word[1]]+=1

          elif len(list_word)==1:
         #print("********",word,"length = ",len(re.findall(r"\b\w+\b",word)))
        
            if len(list_word[0])> 2 and list_word[0] not in stp_word  :
                 dictionnaire_mot[list_word[0]]+=1

 
       dictionnaire[document_numbers[i]]=dictionnaire_mot
  
       dictionnaire_mot=nltk.defaultdict(int)
       i+=1
    
    print(dictionnaire['1'])

    with open('reversed_file_by_docs.json', 'w', encoding='UTF-8') as file_writer:
      json.dump(dictionnaire, file_writer, ensure_ascii=False, sort_keys=False)

    finish = time.time()
    print("***********  time by doc = ",finish-start,'length ',len(dictionnaire)," size ",sys.getsizeof(dictionnaire))


    start=time.time()
    fichier_inverse = {}
    for dic in  dictionnaire.keys():
    
    
        for item in dictionnaire[dic].keys():
   
    
             part1_inverse = (item,int(dic))
         
             fichier_inverse[str(part1_inverse)]=dictionnaire[dic][item]
   
#print(fichier_inverse)
    finish = time.time()
    with open('generic_reverse_file.json', 'w', encoding='UTF-8') as file_writer:
     json.dump(fichier_inverse, file_writer, ensure_ascii=False, sort_keys=False)
    print("***********  inverted file time = ",finish-start,'length ',len(fichier_inverse)," size ",sys.getsizeof(fichier_inverse))


    start=time.time()

    reversed_file_by_words={}
    for doc in dictionnaire.keys():
      for word in dictionnaire[doc].items():
                if word[0] not in reversed_file_by_words.keys():
                    reversed_file_by_words[word[0]] = {}
                reversed_file_by_words[word[0]][doc] = word[1]
    finish = time.time()           
    print("***********  time by word = ",finish-start," nombre word ",len(reversed_file_by_words)," size ",sys.getsizeof(fichier_inverse))


    with open('reversed_file_by_words.json', 'w', encoding='UTF-8') as file_writer:
     json.dump(reversed_file_by_words, file_writer, ensure_ascii=False, sort_keys=False)

