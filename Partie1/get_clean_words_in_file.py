from nltk import word_tokenize
from nltk.corpus import stopwords
import re


def get_clean_words(file_string):

    # words = word_tokenize(file_string)
    words = re.findall(r'\b(.*?)\b', file_string)
    clean_words = []
    for word in words:
        # lower string to match all occurrence
        word = word.lower()
        # remove noisy spaces and special characters
        word = re.sub(r'(\s+|[^a-zA-Z0-9])', '', word)
        # accept only words that are not in stop words
        if word != '' and word not in stopwords.words('english') and len(word) > 1:
            clean_words.append(word.lower())
    return clean_words
