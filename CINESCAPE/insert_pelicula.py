import xlrd
import psycopg2


hostname = 'isilo.db.elephantsql.com'
username = 'hdghyioa'
password = 'crnYUvQbuuWS25aF58t0z01ug--vCCQs'
database = 'hdghyioa'


doc = xlrd.open_workbook('pelicula.xlsx')

doc1 = doc.sheet_by_index(0)

pelicula_nombre = []
pelicula_genero = []
pelicula_idioma = []
pelicula_clasificacion = []
pelicula_duracion = []

for i in range(1, doc1.ncols):
    for j in range(1, doc1.nrows):
        if(i == 1):
            pelicula_nombre.append(repr(doc1.cell_value(j,i)))
        elif(i == 2):
            pelicula_genero.append(repr(doc1.cell_value(j,i)))
        elif(i == 3):
            pelicula_clasificacion.append(repr(int(doc1.cell_value(j,i))))
        elif(i == 4):
            pelicula_duracion.append(repr(int(doc1.cell_value(j,i))))
        elif(i == 5):
            pelicula_idioma.append(repr(doc1.cell_value(j,i)))

# print(pelicula_nombre)
# print(pelicula_genero)
# print(pelicula_clasificacion)
# print(pelicula_duracion)
# print(pelicula_idioma)

DBConnection = None
try:
    print('Connecting to the Cine_AfterOfSaveTheSemester database...')
    print()

    DBConnection = psycopg2.connect(host = hostname, user = username, password = password, dbname = database)
    cursorDB = DBConnection.cursor()

    string = "INSERT INTO pelicula(pelicula_nombre, pelicula_genero, pelicula_idioma, pelicula_clasificacion, pelicula_duracion) VALUES"

    for i in range(len(pelicula_nombre)):
        subquery = string + "({0}, {1}, {2}, {3}, {4})".format(pelicula_nombre[i], pelicula_genero[i], pelicula_idioma[i], pelicula_clasificacion[i], pelicula_duracion[i])
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
