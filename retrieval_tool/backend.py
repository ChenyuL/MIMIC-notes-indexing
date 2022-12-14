import boolean_retriever
import vector_retriever

def search(query=None, num_docs=0, insurance=None, language=None, religion=None, marital_status=None, ethnicity=None, diagnosis=None, gender=None):
   id_list = None
   if insurance or language or religion or marital_status or ethnicity or diagnosis or gender:
      id_list = boolean_retriever.boolean_retrieval(insurance, language, religion, marital_status, ethnicity, diagnosis, gender)
   if not query:
      return id_list
   return vector_retriever.retrieve(query, n=num_docs, ids=id_list)

if __name__ == '__main__':
   boolean_retriever.connect()
   results = search(query='race age', num_docs=0, insurance="Private", ethnicity="WHITE", marital_status="MARRIED", religion="UNOBTAINABLE", gender="F")
   # results = search(query='race age', num_docs=1)
   print(', '.join([str(pair) for pair in results if pair[1]]))
   print(f'Text for id {results[0][0]}:\n' + boolean_retriever.get_text(results[0][0]))
