import xlrd
import psycopg2


hostname = 'isilo.db.elephantsql.com'
username = 'hdghyioa'
password = 'crnYUvQbuuWS25aF58t0z01ug--vCCQs'
database = 'hdghyioa'


doc = xlrd.open_workbook('trabajo.xlsx')

doc1 = doc.sheet_by_index(0)

trabajo_nombre = []

for i in range(1, doc1.ncols):
    for j in range(1, doc1.nrows):
        if(i == 1):
            trabajo_nombre.append(repr(doc1.cell_value(j,i)))

# print(trabajo_nombre)

DBConnection = None
try:
    print('Connecting to the Cine_AfterOfSaveTheSemester database...')
    print()

    DBConnection = psycopg2.connect(host = hostname, user = username, password = password, dbname = database)
    cursorDB = DBConnection.cursor()

    string = "INSERT INTO trabajo(trabajo_nombre) VALUES"

    for i in range(len(trabajo_nombre)):
        subquery = string + "({0})".format(trabajo_nombre[i])
        print(subquery)
        # cursorDB.execute(subquery)

    # DBConnection.commit()

    cursorDB.close()

except(Exception, psycopg2.DatabaseError) as error:
    print('Error encontrado:', error)

finally:
  if DBConnection is not None:
    DBConnection.close()
    print()
    print('Cerrando la conexión a la DB.')
