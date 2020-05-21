import psycopg2
import pandas as Pandas
import random

def query2dataframe(sqlQuery):
    parametrosDatabase = {
        "host":"isilo.db.elephantsql.com",
        "database":"hdghyioa",
        "user":"hdghyioa",
        "password":"crnYUvQbuuWS25aF58t0z01ug--vCCQs"
    }

    DBConnection = None
    resultDataFrame = None
    try:
        print('Connecting to the Cine_AfterOfSaveTheSemester database...')
        DBConnection = psycopg2.connect(**parametrosDatabase)
        resultDataFrame = Pandas.read_sql_query(sqlQuery, DBConnection)
        DBConnection.close()
        return resultDataFrame

    except(Exception, psycopg2.DatabaseError) as error:
        print('Error en el Query:',error)
        return None

    finally:
      if DBConnection is not None:
          DBConnection.close()
      print('Query ejecutado, resultados en un Dataframe.')



fechas = ["'21/05/2020'", "'22/05/2020'", "'23/05/2020'", "'24/05/2020'"]
generos = {"'Terror'":1 , "'Accion'":2, "'Comedia'":3, "'Kids'":4, "'Indie'":5}
funcion_id = [1, 2, 3, 4, 5, 6, 7, 8]


hostname = 'isilo.db.elephantsql.com'
username = 'hdghyioa'
password = 'crnYUvQbuuWS25aF58t0z01ug--vCCQs'
database = 'hdghyioa'

DBConnection = None
try:
    # print('Connecting to the Cine_AfterOfSaveTheSemester database...')
    # print()

    DBConnection = psycopg2.connect(host = hostname, user = username, password = password, dbname = database)
    cursorDB = DBConnection.cursor()

    subquery1 = "DELETE FROM funcionDePelicula"
    cursorDB.execute(subquery1)

    subquery2 = "INSERT INTO funcionDePelicula(funcion_id, funcionDePelicula_fecha, pelicula_id, sala_id) VALUES"

    for i in fechas:
        for j in generos:
            subquery3 = "SELECT * FROM pelicula WHERE pelicula.pelicula_genero = " + j
            pelicula_Dataframe = query2dataframe(subquery3)
            for m in funcion_id:
                num = random.randrange(len(pelicula_Dataframe))
                for row in pelicula_Dataframe.itertuples():
                    if(row[0] == num):
                        subquery4 = subquery2 + "({0}, {1}, {2}, {3})".format(m, i, row[1], generos[j])
                        print(subquery4)
                        cursorDB.execute(subquery4)
            print()

    DBConnection.commit()

    cursorDB.close()

except(Exception, psycopg2.DatabaseError) as error:
    print('Error encontrado:', error)

finally:
  if DBConnection is not None:
    DBConnection.close()
    print()
    print('Cerrando la conexión a la DB.')
