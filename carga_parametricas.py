# coding=utf-8
import sqlite3
import pymssql

class MyDB(object):
    def __init__(self, database):
        self._db_connection = sqlite3.connect(f'databases/{database}/{database}.db')
        self._db_cur = self._db_connection.cursor()

    def parametricQuery(self, query):
        return self._db_cur.execute(query)

    def __del__(self):
        self._db_connection.close()

class CMM_DB(object):
    def __init__(self):
        db_host = '190.145.94.93'
        db_name = 'CMMCRsocialparametricas'
        db_user = 'Arnulforojas'
        db_password = 'Arojas032020'
        self._db_connection = pymssql.connect(server=db_host, user=db_user, password=db_password, database=db_name)
        self._db_cur = self._db_connection.cursor()

    def commit(self, query):
        self._db_cur.execute(query)
        return self._db_connection.commit()

    def __del__(self):
        self._db_connection.close()



def lista_tablas_sqlite():
    db = MyDB('parametric')
    result = db.parametricQuery("SELECT name FROM sqlite_master WHERE type ='table' AND name NOT LIKE 'sqlite_%'").fetchall()
    if result is not None:
        return [res[0] for res in result]

def seleccionar_todo(table):
    db = MyDB('parametric')
    result = db.parametricQuery("SELECT * FROM %s" % table).fetchall()
    return result


def cargar(tabla, info):
    query = "INSERT INTO %s VALUES" % tabla
    db = CMM_DB()
    import sys, io

    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout
    print(query,info)
    output = new_stdout.getvalue()
    sys.stdout = old_stdout
    output = output[:-1]
    print(output)
    db.commit(output)


for tabla in lista_tablas_sqlite():
    for info in seleccionar_todo(tabla):
        cargar(tabla, info)

# Barrios y Actividades de formación


