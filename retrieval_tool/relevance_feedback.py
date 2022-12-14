import backend
import boolean_retriever
import csv
import pandas as pd
import pathlib

if __name__ == '__main__':
   #boolean_retriever.connect()
   rf_file = pd.read_csv(str(pathlib.Path(__file__).parent.absolute()) + '\\Retrieval_true.csv')
   queries = list(rf_file.columns)[1:]
   ids = list(rf_file.iloc[:,0])
   print(ids)
   for i, query in enumerate(queries):
      results = backend.search(' '.join(query.split('_')))
      filtered_results = [(j, *pair) for j, pair in enumerate(results) if pair[1] and pair[0] in ids]
      print(filtered_results)
      with open(str(pathlib.Path(__file__).parent.absolute()) + f'\\results\\{query}.txt', 'w+') as result_file:
         for triplet in filtered_results:
            result_file.write(f'{triplet[0]} {triplet[1]} {triplet[2]} {rf_file.iloc[ids.index(triplet[1]), i+1]}\n')
      
   