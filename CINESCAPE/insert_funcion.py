import xlrd
import psycopg2


hostname = 'isilo.db.elephantsql.com'
username = 'hdghyioa'
password = 'crnYUvQbuuWS25aF58t0z01ug--vCCQs'
database = 'hdghyioa'


doc = xlrd.open_workbook('funcion.xlsx')

doc1 = doc.sheet_by_index(0)

funcion_hora_inicio = []
funcion_hora_fin = []

for i in range(1, doc1.ncols):
    for j in range(1, doc1.nrows):
        if(i == 1):
            funcion_hora_inicio.append(repr(doc1.cell_value(j,i)))
        elif(i == 2):
            funcion_hora_fin.append(repr(doc1.cell_value(j,i)))

# print(funcion_hora_inicio)
# print(funcion_hora_fin)

DBConnection = None
try:
    print('Connecting to the Cine_AfterOfSaveTheSemester database...')
    print()

    DBConnection = psycopg2.connect(host = hostname, user = username, password = password, dbname = database)
    cursorDB = DBConnection.cursor()

    string = "INSERT INTO funcion(funcion_hora_inicio, funcion_hora_fin) VALUES"

    for i in range(len(funcion_hora_fin)):
        subquery = string + "({0}, {1})".format(funcion_hora_inicio[i], funcion_hora_fin[i])
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
