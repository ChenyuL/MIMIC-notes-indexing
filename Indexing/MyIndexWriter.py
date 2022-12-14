import Classes.Path as Path
from collections import Counter

import nltk
from nltk.stem.snowball import SnowballStemmer

# Efficiency and memory cost should be paid with extra attention.
#
# Please add comments along with your code.

class MyIndexWriter:
   
   def __init__(self, type):
      self.index_file = open((Path.NotesDir if type == 'mimic' else print("indexfile error")) + 'index.txt', 'w+', encoding='utf8')
      self.lexicon_file = open((Path.NotesDir if type == 'mimic' else print("indexfile error")) + 'lexicon.txt', 'w+', encoding='utf8')
      self.data = {} # dict: word -> (freq, posting)
   
   # This method build index for each document.
   # NT: in your implementation of the index, you should transform your string docno into non-negative integer docids,
   # and in MyIndexReader, you should be able to request the integer docid for each docno.
   def index(self, docNo, content):
      docId = docNo ## test this
      print("docID", docId)
      for word in content.split():
         if word in self.data: # check if word has been seen before in the collection
            self.data[word][0] += 1 # incrememt collection frequency
            self.data[word][1][docId] += 1 # increment frequency in current document
         else:
            self.data[word] = [1, Counter([docId])] # create new entry in lexicon

   # Close the index writer, and you should output all the buffered content (if any).
   def close(self):
      for word in sorted(self.data.keys()):
         freq, posting = self.data[word]
         self.lexicon_file.write(f'{word} {freq} {self.index_file.tell()}\n') # write to lexicon file
         self.index_file.write(word) # begin new line in index
         for docId, doc_freq in sorted(list(posting.items()), key=lambda x: x[0]):
            self.index_file.write(f' {docId},{doc_freq}') # add all postings for this word
         self.index_file.write('\n')
      self.index_file.close()
      self.lexicon_file.close()
