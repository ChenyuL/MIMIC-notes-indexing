import os
import Classes.Path as Path
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

import numpy as np
class BuildTFiDF ():
    writer = []

    def __init__(self, type):
        path_dir = Path.IndexNotesDir

        os.makedirs(path_dir, exist_ok=True)
        self.DictTfIdf = {}
        self.content = []
        self.Ids = []
        self.DocDict = {}
        with open("buildTfIdf."+str(type)) as f:
            #     for line in f:
            while True:
                thisID = f.readline().replace('\n', '')
                #         print("thisID", thisID)
                thisContent = f.readline().replace('\n', '')
                #         print("thisContent", thisContent)
                self.content.append(thisContent)
                self.Ids.append(thisID)
                self.DocDict.update({thisID: thisContent})
                if not thisID:
                    break
        f.close()

        return

    def get_ifidf_for_words(text):
        tfidf_matrix= tfidf.transform([text]).todense()
        feature_index = tfidf_matrix[0,:].nonzero()[1]
        tfidf_scores = zip([feature_names[i] for i in feature_index], [tfidf_matrix[0, x] for x in feature_index])
        return dict(tfidf_scores)

    def getTfIdfDict(self.DocDict):

        zero_data = np.zeros(shape=(len(self.DocDict), 2))
        dfTFIDF = pd.DataFrame(zero_data, columns=['docID', 'TFIDF'])
        i = 0
        for key, value in self.DocDict.items():
            thisDocID = key
            #     print("thisDocID",thisDocID)
            thisTFIDF = get_ifidf_for_words(value)

            self.DictTfIdf.update({thisDocID: thisTFIDF})