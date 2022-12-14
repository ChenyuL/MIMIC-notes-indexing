import Classes.Path as Path
from sqlalchemy import null
# Efficiency and memory cost should be paid with extra attention.
# Essential private methods or variables can be added.
# Please add comments along with your code.
class WordTokenizer:

    def __init__(self, content):
        # Tokenize the input texts.
        self.contents = content.split(" ")
        self.word = self.contents[0]
        self.index = 0

        return

    def nextWord(self):
        # Return the next word in the document.
        # Return null, if it is the end of the document.
        # word = next(self.content)
        while self.index < len(self.contents):
            # print("len of contents",len(self.contents))
            if self.word is null :
                return None 
            else:
                # print(self.index)
                self.word = self.contents[self.index]
                self.index = self.index +1 
                return self.word

            break