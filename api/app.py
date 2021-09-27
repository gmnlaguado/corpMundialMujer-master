# coding=utf-8
from flask import Flask, request
import os
import pymssql

class MyDB(object):
    def __init__(self):
        db_host = '190.145.94.93'
        db_name = 'CMMCRSocial'
        db_user = 'GeorgeNino'
        db_password = 'Gmnino@2021'
        self._db_connection = pymssql.connect(server=db_host, user=db_user, password=db_password, database=db_name)
        self._db_cur = self._db_connection.cursor()

    def commit(self, query):
        self._db_cur.execute(query)
        return self._db_connection.commit()

    def parametricQuery(self, query):
        return self._db_cur.execute(query)

    def __del__(self):
        self._db_connection.close()



app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Información Operarios</h1>'


@app.route('/actividad_implementacion', methods=['POST'])
def actividad_implementacion():
    informacion = request.json
    info = []
    for item in informacion.values():
        info.append(item)
    info = tuple(info)
    query = "INSERT INTO actividad_implementacion VALUES ('%s','%s','%s','%s',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,'%s',%s,'%s',%s,%s,'%s')" % info
    db = MyDB()
    db.commit(query)
    return f'actividad_implementacion\n\n{query}'


@app.route('/actividad_seguimiento', methods=['POST'])
def actividad_seguimiento():
    informacion = request.json
    info = []
    for item in informacion.values():
        info.append(item)
    info = tuple(info)
    query = "INSERT INTO actividad_seguimiento VALUES ('%s','%s','%s','%s',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,'%s',%s,'%s',%s,%s,'%s')" % info
    db = MyDB()
    db.commit(query)
    return f'actividad_seguimiento\n\n{query}'


@app.route('/beneficiario_proyectos', methods=['POST'])
def beneficiario_proyectos():
    informacion = request.json
    info = []
    for item in informacion.values():
        info.append(item)
    info = tuple(info)
    query = "INSERT INTO beneficiario_proyectos VALUES ('%s','%s','%s','%s','%s',%s,%s,%s,%s,%s,%s,%s,%s,%s)" % info
    db = MyDB()
    db.commit(query)
    return f'beneficiario_proyectos\n\n{query}'


@app.route('/caracterizacion_ampliada', methods=['POST'])
def caracterizacion_ampliada():
    informacion = request.json
    info = []
    for item in informacion.values():
        info.append(item)
    info = tuple(info)
    query = "INSERT INTO caracterizacion_ampliada VALUES ('%s','%s','%s','%s','%s',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,'%s','%s')" % info
    db = MyDB()
    db.commit(query)
    return f'caracterizacion_ampliada\n\n{query}'


@app.route('/caracterizacion_ampliada_informacion_hijos', methods=['POST'])
def caracterizacion_ampliada_informacion_hijos():
    informacion = request.json
    info = []
    for item in informacion.values():
        info.append(item)
    info = tuple(info)
    query = "INSERT INTO caracterizacion_ampliada_informacion_hijos VALUES ('%s','%s','%s','%s',%s,%s,%s,%s)" % info
    db = MyDB()
    db.commit(query)
    return f'caracterizacion_ampliada_informacion_hijos\n\n{query}'


@app.route('/caracterizacion_ampliada_informacion_personas_a_cargo', methods=['POST'])
def caracterizacion_ampliada_informacion_personas_a_cargo():
    informacion = request.json
    info = []
    for item in informacion.values():
        info.append(item)
    info = tuple(info)
    query = "INSERT INTO caracterizacion_ampliada_informacion_personas_a_cargo VALUES ('%s','%s','%s','%s',%s,%s,%s,%s)" % info
    db = MyDB()
    db.commit(query)
    return f'caracterizacion_ampliada_informacion_personas_a_cargo\n\n{query}'


@app.route('/diagnostico_de_perfil_productivo', methods=['POST'])
def diagnostico_de_perfil_productivo():
    informacion = request.json
    info = []
    for item in informacion.values():
        info.append(item)
    info = tuple(info)
    query = "INSERT INTO diagnostico_de_perfil_productivo VALUES ('%s',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" % info
    db = MyDB()
    db.commit(query)
    return f'diagnostico_de_perfil_productivo\n\n{query}'


@app.route('/diagnostico_empresarial', methods=['POST'])
def diagnostico_empresarial():
    informacion = request.json
    info = []
    for item in informacion.values():
        info.append(item)
    info = tuple(info)
    query = "INSERT INTO diagnostico_empresarial VALUES ('%s','%s','%s','%s',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" % info
    db = MyDB()
    db.commit(query)
    return f'diagnostico_empresarial\n\n{query}'


@app.route('/idea_de_negocio', methods=['POST'])
def idea_de_negocio():
    informacion = request.json
    info = []
    for item in informacion.values():
        info.append(item)
    info = tuple(info)
    query = "INSERT INTO idea_de_negocio VALUES ('%s','%s','%s','%s','%s',%s,%s,%s,%s,%s,%s,%s,%s,%s,'%s',%s,'%s',%s,%s,%s,%s,%s,%s,%s,'%s',%s,%s,%s,'%s','%s')" % info
    db = MyDB()
    db.commit(query)
    return f'idea_de_negocio\n\n{query}'


@app.route('/informacion_general_beneficiario', methods=['POST'])
def informacion_general_beneficiario():
    informacion = request.json
    info = []
    for item in informacion.values():
        info.append(item)
    info = tuple(info)
    query = "INSERT INTO informacion_general_beneficiario VALUES ('%s','%s','%s',%s,'%s',%s,'%s',%s,%s,%s,%s,'%s',%s,%s,%s,%s,'%s','%s',%s,%s,'%s',%s,%s,%s,%s,%s,%s,%s,%s)" % info
    db = MyDB()
    db.commit(query)
    return f'informacion_general_beneficiario\n\n{query}'


@app.route('/monitoreo', methods=['POST'])
def monitoreo():
    informacion = request.json
    info = []
    for item in informacion.values():
        info.append(item)
    info = tuple(info)
    query = "INSERT INTO monitoreo VALUES ('%s','%s','%s','%s',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,'%s',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,'%s','%s',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,'%s')" % info
    db = MyDB()
    db.commit(query)
    return f'monitoreo\n\n{query}'


@app.route('/odp_operario', methods=['POST'])
def odp_operario():
    informacion = request.json
    info = []
    for item in informacion.values():
        info.append(item)
    info = tuple(info)
    query = "INSERT INTO odp_operario VALUES ('%s','%s','%s','%s',%s)" % info
    db = MyDB()
    db.commit(query)
    return f'odp_operario\n\n{query}'


@app.route('/odp_operario_proyectos', methods=['POST'])
def odp_operario_proyectos():
    informacion = request.json
    info = []
    for item in informacion.values():
        info.append(item)
    info = tuple(info)
    query = "INSERT INTO odp_operario_proyectos VALUES ('%s','%s','%s')" % info
    db = MyDB()
    db.commit(query)
    return f'odp_operario_proyectos\n\n{query}'


@app.route('/plan_de_formacion', methods=['POST'])
def plan_de_formacion():
    informacion = request.json
    info = []
    for item in informacion.values():
        info.append(item)
    info = tuple(info)
    query = "INSERT INTO plan_de_formacion VALUES ('%s','%s','%s','%s',%s,%s,'%s','%s',%s)" % info
    db = MyDB()
    db.commit(query)
    return f'plan_de_formacion\n\n{query}'


@app.route('/plan_de_implementacion', methods=['POST'])
def plan_de_implementacion():
    informacion = request.json
    info = []
    for item in informacion.values():
        info.append(item)
    info = tuple(info)
    query = "INSERT INTO plan_de_implementacion VALUES ('%s','%s','%s','%s',%s,%s,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % info
    db = MyDB()
    db.commit(query)
    return f'plan_de_implementacion\n\n{query}'


@app.route('/plan_de_seguimiento', methods=['POST'])
def plan_de_seguimiento():
    informacion = request.json
    info = []
    for item in informacion.values():
        info.append(item)
    info = tuple(info)
    query = "INSERT INTO plan_de_seguimiento VALUES ('%s','%s','%s','%s',%s,%s,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % info
    db = MyDB()
    db.commit(query)
    return f'plan_de_seguimiento\n\n{query}'


@app.route('/proyectos', methods=['POST'])
def proyectos():
    informacion = request.json
    info = []
    for item in informacion.values():
        info.append(item)
    info = tuple(info)
    query = "INSERT INTO proyectos VALUES ('%s','%s','%s')" % info
    db = MyDB()
    db.commit(query)
    return f'proyectos\n\n{query}'


@app.route('/unidad_de_negocio', methods=['POST'])
def unidad_de_negocio():
    informacion = request.json
    info = []
    for item in informacion.values():
        info.append(item)
    info = tuple(info)
    query = "INSERT INTO unidad_de_negocio VALUES ('%s','%s','%s','%s','%s',%s,%s,%s,%s,'%s',%s,%s,%s,'%s','%s','%s','%s',%s,'%s','%s',%s,%s,%s,%s,%s,%s,'%s')" % info
    db = MyDB()
    db.commit(query)
    return f'unidad_de_negocio\n\n{query}'


@app.route('/obtener_operarios', methods=['POST'])
def obtener_operarios():
    db = MyDB()
    db.parametricQuery("SELECT document, name, username, password FROM odp_operario")
    result = db._db_cur.fetchall()
    return f'{result}'
    

@app.route('/obtener_operarios_proyectos', methods=['POST'])
def obtener_operarios_proyectos():
    db = MyDB()
    db.parametricQuery("SELECT id, fkOperator, fkProject FROM odp_operario_proyectos")
    result = db._db_cur.fetchall()
    return f'{result}'

if __name__ == "__main__":
    app.run(host= '0.0.0.0')

