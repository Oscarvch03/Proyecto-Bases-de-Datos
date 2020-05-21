import xlrd
import psycopg2


hostname = 'isilo.db.elephantsql.com'
username = 'hdghyioa'
password = 'crnYUvQbuuWS25aF58t0z01ug--vCCQs'
database = 'hdghyioa'


doc = xlrd.open_workbook('empleado.xlsx')

doc1 = doc.sheet_by_index(0)

empleado_id = []
empleado_nombre1 = []
empleado_nombre2 = []
empleado_apellido1 = []
empleado_apellido2 = []
empleado_edad = []
empleado_contraseña = []

for i in range(doc1.ncols):
    for j in range(1, doc1.nrows):
        if(i == 0):
            empleado_id.append(repr(str(int(doc1.cell_value(j,i)))))
        elif(i == 1):
            empleado_nombre1.append(repr(doc1.cell_value(j,i)))
        elif(i == 2):
            empleado_nombre2.append(repr(doc1.cell_value(j,i)))
        elif(i == 3):
            empleado_apellido1.append(repr(doc1.cell_value(j,i)))
        elif(i == 4):
            empleado_apellido2.append(repr(doc1.cell_value(j,i)))
        elif(i == 5):
            empleado_edad.append(repr(int(doc1.cell_value(j,i))))
        elif(i == 6):
            empleado_contraseña.append(repr(doc1.cell_value(j,i)))

# print(empleado_id)
# print(empleado_nombre1)
# print(empleado_nombre2)
# print(empleado_apellido1)
# print(empleado_apellido2)
# print(empleado_edad)
# print(empleado_contraseña)

for k in range(len(empleado_id)):
    if empleado_nombre2[k] == "''":
        empleado_nombre2[k] = 'Null'
# print(empleado_nombre2)


DBConnection = None
try:
    print('Connecting to the Cine_AfterOfSaveTheSemester database...')
    print()

    DBConnection = psycopg2.connect(host = hostname, user = username, password = password, dbname = database)
    cursorDB = DBConnection.cursor()

    string = "INSERT INTO empleado VALUES"

    for i in range(len(empleado_id)):
        subquery = string + "({0}, {1}, {2}, {3}, {4}, {5}, {6})".format(empleado_id[i], empleado_nombre1[i], empleado_nombre2[i], empleado_apellido1[i], empleado_apellido2[i], empleado_edad[i], empleado_contraseña[i])
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
