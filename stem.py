import sys
import nltk
import re
from nltk.stem.porter import PorterStemmer

if len(sys.argv) != 2:
    raise Exception("Usage: python3 " + sys.argv[0] + " [file.txt]")
with open(sys.argv[1], "r") as f:
    data = f.read()

tokens = nltk.word_tokenize(data)
words = [token for token in tokens if re.match(r'^[a-z]+$', token)]
unique_words = list(set(words))

stemmer = PorterStemmer()
for word in unique_words:
    stem = stemmer.stem(word)
    print("{:<20}{:<20}{:1}".format(word, stem, "*" if word != stem else ""))
