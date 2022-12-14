import Classes.Path as Path
import pandas as pd 

# Efficiency and memory cost should be paid with extra attention.
# Essential private methods or variables can be added.
# Please add comments along with your code.
class StopWordRemover:


    def __init__(self):
        # Load and store the stop words from the fileinputstream with appropriate data structure.
        # # NT: address of stopword.txt is Path.StopwordDir.
        # read stop words file
        self.StopWordFile = open("./"+Path.StopwordDir,"r")
        self.StopWords = self.StopWordFile.read()
        # convert StopWords file into a list
        self.StopWords_list = self.StopWords.split("\n")
        # print(self.StopWords_list)
        
        return

    def isStopword(self, word):
        
        #if the word is in the StopWord list return True 
        if (word in self.StopWords_list):
            # print(word)
            return True
        else:
            # print("not stop word")
        # Return true if the input word is a stopword, or false if not.
            return False
