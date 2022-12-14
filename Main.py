import Indexing.PreProcessedCorpusReader as PreprocessedCorpusReader
# import Indexing.HW3IndexWriter  as MyIndexWriter
import Indexing.MyIndexWriter as MyIndexWriter
import Indexing.HW3IndexReader as MyIndexReader
import datetime
import re

#

import PreprocessData.MIMICNotesCollection as MIMICNotesCollection

import PreprocessData.StopWordRemover as StopWordRemover
import PreprocessData.WordNormalizer as WordNormalizer
import PreprocessData.WordTokenizer as WordTokenizer
import Classes.Path as Path
import datetime


# !!! YOU CANNOT CHANGE ANYTHING IN THIS CLASS !!! This is for INFSCI 2140 in Fall 2022

def PreProcess(collectionType):
    # Open the collection by type.
    if collectionType == "mimic":
        collection = MIMICNotesCollection.MIMICCollection()
    else:
        # collection = TrecwebCollection.TrecwebCollection()
        print("wrong collection")

    # Initialize essential objects.
    stopwordRemover = StopWordRemover.StopWordRemover()

    normalizer = WordNormalizer.WordNormalizer()

    wr = open(Path.ResultHM1 + collectionType, "w", encoding="utf8")
    doc = []
    print(collection)
    # Process the corpus, document by document, iteratively.
    count = 0
    while True:
        doc = collection.nextDocument()
        if doc == None or doc == ["", ""]:
            break
        docNo = doc[0]
        # print(docNo)
        content = doc[1]
        # print(content)
        # Output the docNo.
        wr.write(docNo + "\n")

        # Output the preprocessed content.
        tokenizer = WordTokenizer.WordTokenizer(content)

        # print(tokenizer)
        while True:
            word = tokenizer.nextWord()
            ### add delete numbers

            # print(word)
            if word == None:
                break

            if word.isnumeric():
                continue

            # remove any number  corpus
            if re.search('[0-9]', word) is not None:
                continue

            word = normalizer.lowercase(word)
            # print("word",word)
            if stopwordRemover.isStopword(word) == False:
                wr.write(normalizer.stem(word) + " ")


        wr.write("\n")
        count += 1
        if count % 10000 == 0:
            print("finish %s docs" % count)
    wr.close()
    print("Total : %s docs" % count)
    return

startTime = datetime.datetime.now()
PreProcess("mimic")



def WriteIndex(type):
    count = 0
    # Initiate pre-processed collection file reader.
    corpus =PreprocessedCorpusReader.PreprocessedCorpusReader(type)
    # Initiate the index writer.
    indexWriter = MyIndexWriter.MyIndexWriter(type)
    # Build index of corpus document by document.
    while True:
        doc = corpus.nextDocument()
        print("doc", doc)
        if doc == None:
            break
        print(doc[0])
        indexWriter.index(doc[0], doc[1])
        count+=1
        if count%30000==0:
            print("finish ", count," docs")
    print("totally finish ", count, " docs")
    indexWriter.close()
    return


def ReadIndex(type, token):
    # Initiate the index file reader.
    idx =MyIndexReader.MyIndexReader(type)
    # retrieve the token.
    df = idx.DocFreq(token)
    ctf = idx.CollectionFreq(token)
    print(" >> the token \""+token+"\" appeared in "+ str(df) +" documents and "+ str(ctf) +" times in total")
    if df>0:
        posting = idx.getPostingList(token)
        for docId in posting:
            docNo = idx.getDocNo(docId)
            print(docNo+"\t"+str(docId)+"\t"+str(posting[docId]))
# # ReadIndex("mimic")
# startTime = datetime.datetime.now()
# WriteIndex("mimic")
# endTime = datetime.datetime.now()
# print ("mimic running time: ", endTime - startTime)
