import psycopg2
import pandas as pd 

db_name = 'mimic'
username = 'postgres'
pword = '05170029LCy'

cnn = None
cursor = None
# 'connection = psycopg2.connect(database='mimic',
#                         host='::1",
#                         user='postgres',
#                         password='05170029LCy',
#                         port='5432')
# this needs to be ran before extracting data
def connect(dbname=db_name, user=username, password=pword):
   global conn, cursor
   conn = psycopg2.connect(dbname=dbname, user=user, password=password)
   cursor = conn.cursor()
   cursor.execute("SET search_path TO mimiciii;")

# Get a list of discharge reports that match the specified constraints
def boolean_retrieval(insurance=None, language=None, religion=None, marital_status=None, ethnicity=None, diagnosis=None, gender=None):
   
   conditions = []
   values = []
   join_admissions = False
   join_patients = False
   
   # add conditions if arguments are given
   if insurance:
      join_admissions = True
      conditions.append("insurance = (%s)")
      values.append(insurance)
   if language:
      join_admissions = True
      conditions.append("language = (%s)")
      values.append(language)
   if religion:
      join_admissions = True
      conditions.append("religion = (%s)")
      values.append(religion)
   if marital_status:
      join_admissions = True
      conditions.append("marital_status = (%s)")
      values.append(marital_status)
   if ethnicity:
      join_admissions = True
      conditions.append("ethnicity = (%s)")
      values.append(ethnicity)
   if diagnosis:
      join_admissions = True
      conditions.append("diagnosis = (%s)")
      values.append(diagnosis)
   if gender:
      join_patients = True
      conditions.append("gender = (%s)")
      values.append(gender)
   
   # if no constraints are given, everything would be returned, so there is no point in running the query
   if not join_admissions and not join_patients:
      return
   
   # build the whole query
   query = "SELECT DISTINCT noteevents.row_id FROM noteevents"
   
   # join with other tables as needed
   if join_admissions:
      query += " FULL JOIN admissions ON admissions.subject_id = noteevents.subject_id"
   if join_patients:
      query += " FULL JOIN patients ON patients.subject_id = noteevents.subject_id"
   
   query += " WHERE category = 'Discharge summary' AND description = 'Report'"
   
   if conditions:
      query += f" AND {' AND '.join(conditions)}"
   query += ';'
   
   # execute the query
   print(query)
   cursor.execute(query, values)
   
   ids = []
   for row in cursor:
      #print(row[0])
      ids.append(row[0])
      
   return ids

# get text of discharge report given its id
def get_text(id):
   #print(id)
   idlist = tuple(id)
   print("idlist",idlist)
   cursor.execute("SELECT text FROM noteevents WHERE row_id IN %s", [idlist])
   for row in cursor:
      return row[0]

def get_structured(id):
   idlist = tuple(id)
   cursor.execute("""SELECT A.row_id as adm_row_id, N.row_id as note_row_id, A.subject_id, A.hadm_id, admittime, dischtime, gender, dod, insurance, language, religion, marital_status, ethnicity,  diagnosis
	                  FROM mimiciii.noteevents N
	                  LEFT JOIN mimiciii.admissions A on N.hadm_id = A.hadm_id and N.subject_id = A.subject_id
	                  LEFT JOIN mimiciii.patients P on P.subject_id = A.subject_id
	                  WHERE N.row_id IN  %s""", [idlist])
   colnames = [desc[0] for desc in cursor.description]
   df = pd.DataFrame(cursor.fetchall(),columns=colnames)
   return df
if __name__ == '__main__':
   connect()
   # this query allows the connection to access the database properly
   id_list = boolean_retrieval(insurance="Private", ethnicity="WHITE", marital_status="MARRIED", religion="UNOBTAINABLE", gender="F")
   # print("gettext", get_text(id_list))
   # print("getStructured", get_structured(id_list))
   print(id_list)
   #print(get_text(id_list[0]))
