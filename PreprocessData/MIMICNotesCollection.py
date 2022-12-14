# from sqlalchemy import null
import Classes.Path as Path
from bs4 import BeautifulSoup
import string


# Efficiency and memory cost should be paid with extra attention.
# Essential private methods or variables can be added.
# Please add comments along with your code.

class MIMICCollection:

    def __init__(self):
        # 1. Open the file in Path.DataTextDir.
        # 2. Make preparation for function nextDocument().
        # NT: you cannot load the whole corpus into memory!!
        self.f = open("./" + Path.MIMICNotes , 'r+')

        return

    def nextDocument(self):
        #         print(self.f.tell())
        # 1. When called, this API processes one document from corpus, and returns its doc number and content.
        # 2. When no document left, return , and close the filedafsd
        try:
            # if(self.line_number <= self.file_length-1):
            content = ''
            while True:
                line = next(self.f).strip("\n")

                # print(line)
                if (line != "</DOC>"):
                    content = content + str(line) + " "
                if (line == "</DOC>"):
                    content = content + str("</DOC>")
                    break
                # self.line_number = self.line_number + 1
                # print(self.line_number)
            #            print("final content", content)
            soup = BeautifulSoup(content, 'lxml')
            doccontent = soup.body.text[37:]
            doccontent = doccontent.translate(str.maketrans('', '', string.punctuation))
            # print(doccontent)
            docNo = str(soup.body.docno.contents)
            # print(type(docNo))
            return [docNo, doccontent]

        except StopIteration as e:

            return None


