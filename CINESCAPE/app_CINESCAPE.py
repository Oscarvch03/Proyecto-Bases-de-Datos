import flask
from flask import Flask, redirect, url_for, request, render_template
import pandas as Pandas
import psycopg2

app = flask.Flask(__name__)
app.config["DEBUG"] = True

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
        # print('Connecting to the Cine_AfterOfSaveTheSemester database...')
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
      # print('Query ejecutado, resultados en un Dataframe.')


def insert_database(sqlQuery):
    parametrosDatabase = {
        "host":"isilo.db.elephantsql.com",
        "database":"hdghyioa",
        "user":"hdghyioa",
        "password":"crnYUvQbuuWS25aF58t0z01ug--vCCQs"
    }

    DBConnection = None
    resultDataFrame = None
    try:
        # print('Connecting to the Cine_AfterOfSaveTheSemester database...')
        DBConnection = psycopg2.connect(**parametrosDatabase)

        cursorDB = DBConnection.cursor()

        string = sqlQuery

        cursorDB.execute(string)

        DBConnection.commit()

    except(Exception, psycopg2.DatabaseError) as error:
        print('Error en el Query:',error)

    finally:
      if DBConnection is not None:
          DBConnection.close()
      # print('Query ejecutado, resultados en un Dataframe.')


################################################################################

fechas = ["'21/05/2020'", "'22/05/2020'", "'23/05/2020'", "'24/05/2020'"]
generos = ["'Terror'", "'Accion'", "'Comedia'", "'Kids'", "'Indie'"]


@app.route('/', methods = ['GET'])
def paginaInicial():
    out = "<h1> Bienvenidos, CINESCAPE <//h1>"
    out += "<h2> Las funciones programadas son: <//h2>"
    for i in fechas:
        out += "<p> {0} <///p>".format(i[1:-1])
        for j in generos:
            out += "<p> {0} </p>".format(j[1:-1])
            query1 = """ SELECT pelicula_nombre AS Pelicula, pelicula_idioma AS Idioma, funcion_hora_inicio AS Inicio, funcion_hora_fin AS Fin
                         FROM funcionDePelicula JOIN pelicula ON funcionDePelicula.pelicula_id = pelicula.pelicula_id
                                                JOIN funcion ON funcionDePelicula.funcion_id = funcion.funcion_id
                         WHERE funcionDePelicula.funcionDePelicula_fecha = {0} AND pelicula.pelicula_genero = {1} """.format(i, j)
            dataframe = query2dataframe(query1)
            # print(dataframe)
            out += "<p> " + dataframe.to_html() + " </p>"
        out += "<p> <///p>"
    return(out)


@app.route('/registro/', methods = ['GET'])
def registro():
    return app.send_static_file('registro.html')


@app.route('/registrarse', methods = ['POST', 'GET'])
def registrarse():
    if request.method == 'POST':
        cliente_id = request.values.get("cliente_id")
        cliente_nombre1 = request.values.get("cliente_nombre1")
        cliente_nombre2 = request.values.get("cliente_nombre2")
        cliente_apellido1 = request.values.get("cliente_apellido1")
        cliente_apellido2 = request.values.get("cliente_apellido2")
        cliente_edad = int(request.values.get("cliente_edad"))
        cliente_telefono = request.values.get("cliente_telefono")
        cliente_contraseña = request.values.get("cliente_contraseña")

        query = "INSERT INTO cliente VALUES('{0}', '{1}', '{2}', '{3}', '{4}', {5}, '{6}', '{7}')".format(cliente_id, cliente_nombre1, cliente_nombre2, cliente_apellido1, cliente_apellido2, cliente_edad, cliente_telefono, cliente_contraseña)

        if cliente_nombre2 == "":
            cliente_nombre2 = 'Null'
            query = "INSERT INTO cliente VALUES('{0}', '{1}', {2}, '{3}', '{4}', {5}, '{6}', '{7}')".format(cliente_id, cliente_nombre1, cliente_nombre2, cliente_apellido1, cliente_apellido2, cliente_edad, cliente_telefono, cliente_contraseña)

        insert_database(query)

        out = "<p> Ha sido registrado con exito. </p>"
        return(out)


@app.route('/reserva/', methods = ['GET'])
def reserva():
    return app.send_static_file('reserva.html')


@app.route('/reservar', methods = ['POST', 'GET'])
def reservar():
    if request.method == 'POST':
        cliente_id = request.values.get("cliente_id")
        pelicula_nombre = request.values.get("pelicula_nombre")
        hora_inicio = request.values.get("funcion_hora_inicio")

        query1 = "SELECT pelicula_id FROM pelicula WHERE pelicula_nombre = '{0}'".format(pelicula_nombre)
        query2 = "SELECT funcion_id FROM funcion  WHERE funcion_hora_inicio = '{0}'".format(hora_inicio)

        # print(query1)
        # print(query2)

        dataframe1 = query2dataframe(query1)
        dataframe2 = query2dataframe(query2)

        data1 = 0
        for row1 in dataframe1.itertuples():
            data1 = row1[1]

        data2 = 0
        for row2 in dataframe2.itertuples():
            data2 = row2[1]

        query3 = "INSERT INTO reservaDeFuncion(cliente_id, pelicula_id, funcion_id) VALUES('{0}', {1}, {2})".format(cliente_id, data1, data2)

        insert_database(query3)

        out = "<p> Has reservado con exito. </p>"

        return(out)

app.run()
