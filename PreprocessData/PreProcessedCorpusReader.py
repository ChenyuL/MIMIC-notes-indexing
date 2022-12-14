import Classes.Path as Path


class PreprocessedCorpusReader:

    corpus = 0

    def __init__(self, type):
        self.corpus = open(Path.ResultHM1+str(type), "r+", encoding="utf8")
        print("corpusreader",self.corpus)

    def nextDocument(self):
        docNo=self.corpus.readline().strip()
        print("docNo", docNo)
        if docNo=="":
            self.corpus.close()
            return
        content=self.corpus.readline().strip()
        print("content", content)
        return [docNo, content]
