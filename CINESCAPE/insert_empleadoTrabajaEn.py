import xlrd
import psycopg2


hostname = 'isilo.db.elephantsql.com'
username = 'hdghyioa'
password = 'crnYUvQbuuWS25aF58t0z01ug--vCCQs'
database = 'hdghyioa'


doc = xlrd.open_workbook('empleadoTrabajaEn.xlsx')

doc1 = doc.sheet_by_index(0)

empleado_id = []
trabajo_id = []
sueldo = []

for i in range(doc1.ncols):
    for j in range(1, doc1.nrows):
        if(i == 0):
            empleado_id.append(repr(str(int(doc1.cell_value(j,i)))))
        elif(i == 1):
            trabajo_id.append(repr(int(doc1.cell_value(j,i))))
        elif(i == 2):
            sueldo.append(repr(doc1.cell_value(j,i)))


# print(empleado_id)
# print(trabajo_id)
# print(sueldo)


DBConnection = None
try:
    print('Connecting to the Cine_AfterOfSaveTheSemester database...')
    print()

    DBConnection = psycopg2.connect(host = hostname, user = username, password = password, dbname = database)
    cursorDB = DBConnection.cursor()

    string = "INSERT INTO empleadoTrabajaEn(empleado_id, trabajo_id, sueldo) VALUES"

    for i in range(len(empleado_id)):
        subquery = string + "({0}, {1}, {2})".format(empleado_id[i], trabajo_id[i], sueldo[i])
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
