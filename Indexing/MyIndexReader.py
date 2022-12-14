import Classes.Path as Path

# Efficiency and memory cost should be paid with extra attention.
#
# Please add comments along with your code.
class MyIndexReader:
   def __init__(self, type):
      self.type = type
      self.index_file = open((Path.NotesDir if type == 'mimic' else print("readindex error")) + 'index.txt', 'r', encoding='utf8')
      self.lexicon = {}
      for line in open((Path.NotesDir if type == 'mimic' else print("readindex error")) + 'lexicon.txt', 'r', encoding='utf8').read().split('\n'):
         if line:
            word, freq, loc = line.split()
            self.lexicon[word] = (int(freq), int(loc))
      print('finish reading the index')

   # Return the integer DocumentID of input string DocumentNo.
   def getDocId(self, docNo):
      return int('1' + ''.join([c for c in docNo if c.isnumeric()]))

   # Return the string DocumentNo of the input integer DocumentID.
   def getDocNo(self, docId):
      doc = str(docId)[1:]
      if self.type == 'mimic':
         return
      return
   
   # Return DF.
   def DocFreq(self, token):
      self.index_file.seek(self.lexicon[token][1]) # seek to location of the token's posting
      return len(self.index_file.readline().split()) - 1
   
   # Return the frequency of the token in whole collection/corpus.
   def CollectionFreq(self, token):
      return self.lexicon[token][0]
   
   # Return posting list in form of {documentID:frequency}.
   def getPostingList(self, token):
      self.index_file.seek(self.lexicon[token][1]) # seek to location of the token's posting
      return {int(pair.split(',')[0]): int(pair.split(',')[1]) for pair in self.index_file.readline().split() if ',' in pair}
