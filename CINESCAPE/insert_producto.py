import xlrd
import psycopg2


hostname = 'isilo.db.elephantsql.com'
username = 'hdghyioa'
password = 'crnYUvQbuuWS25aF58t0z01ug--vCCQs'
database = 'hdghyioa'


doc = xlrd.open_workbook('producto.xlsx')

doc1 = doc.sheet_by_index(0)

producto_nombre = []
producto_precio = []

for i in range(1, doc1.ncols - 1):
    for j in range(1, doc1.nrows):
        if(i == 1):
            producto_nombre.append(repr(doc1.cell_value(j,i)))
        elif(i == 2):
            producto_precio.append(repr(float(doc1.cell_value(j,i))))

# print(producto_nombre)
# print(producto_precio)

DBConnection = None
try:
    print('Connecting to the Cine_AfterOfSaveTheSemester database...')
    print()

    DBConnection = psycopg2.connect(host = hostname, user = username, password = password, dbname = database)
    cursorDB = DBConnection.cursor()

    string = "INSERT INTO producto(producto_nombre, producto_precio) VALUES"

    for i in range(len(producto_nombre)):
        subquery = string + "({0}, {1})".format(producto_nombre[i], producto_precio[i])
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
