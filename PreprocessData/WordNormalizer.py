import Classes.Path as Path
import nltk
from nltk.stem.snowball import SnowballStemmer


# Efficiency and memory cost should be paid with extra attention.
# Essential private methods or variables can be added.
# Please add comments along with your code.
class WordNormalizer:

    def __init__(self):
    
        return

    def lowercase(self, word):
        # Transform the word uppercase characters into lowercase.
        # print(word)
        self.word = word.lower()
        # print(word) 
        return self.word

    def stem(self, word):
        stemmer = SnowballStemmer(language='english')
        self.word = stemmer.stem(word)
        # Return the stemmed word with PorterStemmer imported previously.
        return self.word
