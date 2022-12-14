import heapq
from numba import njit
from numba.typed import Dict
import numpy as np
import pathlib
import pickle as pkl
import time
from nltk.stem.snowball import SnowballStemmer

current_directory = str(pathlib.Path(__file__).parent.absolute())
vector_file = open(current_directory + '\\vectors.txt', 'r', encoding='utf8')
lexicon_file = open(current_directory + '\\corpus.txt', 'r', encoding='utf8')
lexicon_file.seek(0)
token_list = [line.strip() for line in lexicon_file.read().split('\n') if line]
token_index = Dict()
token_index.update({token: i for i, token in enumerate(token_list)})

stemmer = SnowballStemmer(language='english')

curr_time = time.time()
def starttime():
   global curr_time
   curr_time = time.time()

def printtime():
   print('TIME: ' + str(time.time() - curr_time))

# load pickled vectorizer model
with open(current_directory + '\\TFIDF_vectorizer.pkl', 'rb') as pickled_vectorizer:
   vectorizer = pkl.load(pickled_vectorizer)

# Return posting list in form of {documentID:tfidf}.
@njit
def get_vector(line, token_index):
   #starttime()
   #vector = sparse.csr_array((1, len(token_list)))
   vector = []
   #print(vector.shape)
   for pair in line:
      token, n = pair.split(':')
      vector.append((token_index[token], n))
   #printtime()
   return vector

a_big = None
a_norm = None
a_keys = None
# cosine similarity between query and document b
def similarity(b):
   b_norm = sum([float(i[1]) ** 2 for i in b]) ** 0.5
   dot_product = 0
   for k in b:
      if k[0] in a_keys:
         dot_product += float(k[1]) * a_big[k[0]]
   try:
      return dot_product / (a_norm * b_norm)
   except ZeroDivisionError:
      return 0

def preprocess(query):
   return [' '.join([stemmer.stem(word) for word in query.lower().split() if word])]

# convert a query into a vector with tf-idf weights
def vectorize(query):
   processed_query = preprocess(query)
   print(processed_query)
   vector = np.zeros(len(token_list))
   # create sparse matrix from query
   matrix = vectorizer.transform(processed_query)
   print(list(matrix[0, :]))
   return matrix

# return n most relevant docs for query
def retrieve(query, n=0, ids=None):
   starttime()
   query_vector = vectorize(query)
   print(query_vector)
   query_vector = dict(query_vector.todok().items())
   query_dict = {}
   for k in query_vector.keys():
      query_dict[k[1]] = query_vector[k]
   a = list(query_dict.items())
   # do part of the cosine similarity calculation in advance
   global a_norm, a_big, a_keys
   a_norm = sum([float(i[1]) ** 2 for i in a]) ** 0.5
   a_big = np.zeros((len(token_list)))
   a_keys = [i[0] for i in a]
   for i in a:
      a_big[i[0]] = float(i[1])
   scores = {}
   vector_file.seek(0)
   while True:
      line = vector_file.readline()
      if not line:
         break
      vec = line.strip().split()
      try:
         doc = int(vec.pop(1))
         if ids and doc not in ids:
            continue
      except IndexError:
         continue
      #print('doc: ', doc)
      vec = vec[2:]
      #print(len(vec))
      #scores[doc] = similarity(list(get_vector(vec).items()), list(query_dict.items()))
      b = get_vector(vec, token_index)
      scores[doc] = similarity(b)
      '''if scores[doc]:
         print(doc, scores[doc])'''
   if n:
      return heapq.nlargest(n, scores.items(), key=lambda s: s[1])
   return sorted(scores.items(), key=lambda s: s[1], reverse=True)

if __name__ == '__main__':
   print(retrieve('race age', n=2))
   printtime()
