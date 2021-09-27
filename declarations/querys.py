# coding=utf-8
import sqlite3


class MyDB(object):
    def __init__(self, database):
        self._db_connection = sqlite3.connect(f'databases/{database}/{database}.db')
        self._db_cur = self._db_connection.cursor()

    def query(self, query, params):
        return self._db_cur.execute(query, params)

    def parametricQuery(self, query):
        return self._db_cur.execute(query)

    def commit(self, query, params):
        self._db_cur.execute(query, params)
        return self._db_connection.commit()

    def fast_commit(self, query):
        self._db_cur.execute(query)
        return self._db_connection.commit()

    def __del__(self):
        self._db_connection.close()


# Register
# Select

def idOperator(username):
    db = MyDB('register')
    result = db.query("SELECT document FROM odp_operario WHERE username = :username", {'username': username}).fetchone()
    if result is not None:
        return result[0]


def idProject(project):
    db = MyDB('register')
    result = db.query("SELECT id FROM proyectos WHERE name = :project", {'project': project}).fetchone()
    if result is not None:
        return result[0]


def payeeProjects(project):
    db = MyDB('register')
    result = db.query("SELECT payeeDocument FROM beneficiario_proyectos WHERE project = :project",
                      {'project': project}).fetchall()
    if result is not None:
        return [res[0] for res in result]


def passwordOperator(document):
    db = MyDB('register')
    result = db.query("SELECT password FROM odp_operario WHERE document = :document", {'document': document}).fetchone()
    if result is not None:
        return result[0]


def projectsOperator(document):
    db = MyDB('register')
    result = db.query("SELECT fkProject FROM odp_operario_proyectos WHERE fkOperator = :document",
                      {'document': document}).fetchall()
    if result is not None:
        return [res[0] for res in result]


def nameProject(project):
    db = MyDB('register')
    result = db.query("SELECT name FROM proyectos WHERE id = :project", {'project': project}).fetchone()
    if result is not None:
        return result[0]


def bringData(table):
    db = MyDB('register')
    result = db.parametricQuery("SELECT * FROM %s" % table).fetchall()
    return result


def tipo_de_beneficiario(beneficiario):
    db = MyDB('register')
    result = db.query("SELECT payeeType FROM informacion_general_beneficiario WHERE document = :beneficiario",
                      {'beneficiario': beneficiario}).fetchone()
    if result is not None:
        return result[0]


def plan_de_formacion_habilitado(beneficiario):
    db = MyDB('register')
    result = db.query("SELECT plan_de_formacion FROM beneficiario_proyectos WHERE payeeDocument = :beneficiario",
                      {'beneficiario': beneficiario}).fetchone()
    if result is not None:
        return result[0]


def plan_de_implementacion_habilitado(beneficiario):
    db = MyDB('register')
    result = db.query("SELECT plan_de_implementacion FROM beneficiario_proyectos WHERE payeeDocument = :beneficiario",
                      {'beneficiario': beneficiario}).fetchone()
    if result is not None:
        return result[0]


def etapa_del_proceso(beneficiario):
    db = MyDB('register')
    result = db.query("SELECT etapa_del_proceso FROM beneficiario_proyectos WHERE payeeDocument = :beneficiario",
                      {'beneficiario': beneficiario}).fetchone()
    if result is not None:
        return result[0]


def traer_actividades_formacion(beneficiario, proyecto):
    db = MyDB('register')
    result = db.query(
        "SELECT id_actividad, fecha_actividad, completada FROM plan_de_formacion WHERE beneficiario = :beneficiario AND proyecto = :proyecto",
        {'beneficiario': beneficiario, 'proyecto': proyecto}).fetchall()
    if result is not None:
        return [list(res) for res in result]


def comprobar_plan_de_formacion(beneficiario, project):
    db = MyDB('register')
    result = db.query(
        "SELECT concluido_formacion FROM beneficiario_proyectos WHERE payeeDocument = :beneficiario AND project = :project",
        {'beneficiario': beneficiario, 'project': project}).fetchone()
    if result is not None:
        return result[0]


def comprobar_plan_de_implementacion(beneficiario, project):
    db = MyDB('register')
    result = db.query(
        "SELECT concluido_implementacion FROM beneficiario_proyectos WHERE payeeDocument = :beneficiario AND project = :project",
        {'beneficiario': beneficiario, 'project': project}).fetchone()
    if result is not None:
        return result[0]


def comprobar_monitoreo(beneficiario, project):
    db = MyDB('register')
    result = db.query(
        "SELECT monitoreo FROM beneficiario_proyectos WHERE payeeDocument = :beneficiario AND project = :project",
        {'beneficiario': beneficiario, 'project': project}).fetchone()
    if result is not None:
        return result[0]


def traer_puntajes_diagnostico(beneficiario, project):
    db = MyDB('register')
    result = db.query(
        "SELECT categoria_1, categoria_2, categoria_3, categoria_4, categoria_5, categoria_6, categoria_7, categoria_8, categoria_9  FROM diagnostico_empresarial WHERE fk_beneficiario = :beneficiario AND fk_proyecto = :project",
        {'beneficiario': beneficiario, 'project': project}).fetchone()
    return list(result)


def ver_cuantas_visitas(beneficiario, project):
    db = MyDB('register')
    result = db.query(
        "SELECT numero_de_visitas, numero_realizadas FROM plan_de_implementacion WHERE payeeDocument = :beneficiario AND project = :project",
        {'beneficiario': beneficiario, 'project': project}).fetchone()
    return result


def traer_metas_implementacion(beneficiario, proyecto):
    db = MyDB('register')
    result = db.query("SELECT meta_1, meta_2, meta_3, meta_4, meta_5, meta_6, meta_7, meta_8, meta_9 FROM "
                      "plan_de_implementacion WHERE payeeDocument = :beneficiario AND project = :project",
                      {'beneficiario': beneficiario, 'project': proyecto}).fetchone()
    return list(result)


def lista_de_caracterizaciones(project):
    db = MyDB('register')
    result = db.query("SELECT document FROM caracterizacion_ampliada WHERE project = :project",
                      {'project': project}).fetchall()
    if result is not None:
        return [res[0] for res in result]


def obtener_estado(beneficiario):
    db = MyDB('register')
    result = db.query("SELECT status FROM beneficiario_proyectos WHERE payeeDocument = :beneficiario",
                      {'beneficiario': beneficiario}).fetchone()
    if result is not None:
        return result[0]


def consulta_beneficiario(beneficiario, proyecto, tabla):
    db = MyDB('register')
    query1 = "SELECT * FROM %s" % tabla
    result = db.query(query1 + " WHERE document = :beneficiario AND project = :proyecto",
                      {'beneficiario': beneficiario, 'proyecto': proyecto}).fetchall()
    if result is not None and len(result)>0:
        return result[0]


# Register
# Insert Into

def cargar(tabla, columnas, info):
    columnas -= 1
    db = MyDB('register')
    query = "INSERT INTO %s VALUES" + " (?" + ", ?" * columnas + ")"
    db.commit(query % tabla, info)


# Register
# Update


def registrar(tabla, columna, beneficiario, proyecto, valor):
    db = MyDB('register')
    db.commit("UPDATE %s SET %s = :valor WHERE payeeDocument = :beneficiario AND "
              "project = :project" % (tabla, columna), (valor, beneficiario, proyecto))


def dar_actividad_de_formacion_como_finalizada(beneficiario, project, actividad, fecha):
    db = MyDB('register')
    db.commit(
        "UPDATE plan_de_formacion SET completada = 1, fecha_realizada = :fecha WHERE beneficiario = :beneficiario AND proyecto = :project AND id_actividad = :actividad",
        (fecha, beneficiario, project, actividad))


def sumar_una_actividad(beneficiario, project):
    db = MyDB('register')
    result = db.query(
        "SELECT numero_realizadas FROM plan_de_implementacion WHERE payeeDocument = :beneficiario AND project = :project",
        {'beneficiario': beneficiario, 'project': project}).fetchone()
    if result is not None:
        result = result[0]
        result += 1
        db.commit(
            "UPDATE plan_de_implementacion SET numero_realizadas = :result WHERE payeeDocument = :beneficiario AND project = :project",
            (result, beneficiario, project))


# Parametric
# Select


def traer_id_de_actividad_de_formacion(actividad):
    db = MyDB('parametric')
    result = db.query("SELECT id FROM actividades_de_formacion WHERE description = :actividad",
                      {'actividad': actividad}).fetchone()
    if result is not None:
        return result[0]


def indicator(department):
    db = MyDB('parametric')
    result = db.query("SELECT indicative FROM departamentos WHERE id = :department",
                      {'department': department}).fetchone()
    if result is not None:
        return result[0]


def parametricList(tabl):
    db = MyDB('parametric')
    result = db.parametricQuery("SELECT data FROM %s" % tabl).fetchall()
    if result is not None:
        return [res[0] for res in result]


def idParametrics(table, data):
    db = MyDB('parametric')
    result = db.parametricQuery("SELECT id FROM %s WHERE data = '%s'" % (table, data)).fetchone()
    if result is not None:
        return result[0]


def dataParametrics(table, ids):
    db = MyDB('parametric')
    result = db.parametricQuery("SELECT data FROM %s WHERE id = '%s'" % (table, ids)).fetchone()
    if result is not None:
        return result[0]


def bringDepartments(country):
    db = MyDB('parametric')
    result = db.query("SELECT data FROM departamentos WHERE fkCountry = :country", {'country': country}).fetchall()
    if result is not None:
        return [res[0] for res in result]


def idDepartments(department):
    db = MyDB('parametric')
    result = db.query("SELECT id FROM departamentos WHERE data = :department", {'department': department}).fetchone()
    if result is not None:
        return result[0]


def bringCities(department):
    db = MyDB('parametric')
    result = db.query("SELECT data FROM ciudades WHERE fkDepartment = :department",
                      {'department': department}).fetchall()
    if result is not None:
        return [res[0] for res in result]


def idCities(city):
    db = MyDB('parametric')
    result = db.query("SELECT id FROM ciudades WHERE data = :city", {'city': city}).fetchone()
    if result is not None:
        return result[0]


def bringNeighborhoods(city):
    db = MyDB('parametric')
    result = db.query("SELECT data FROM barrios WHERE fkCities = :city", {'city': city}).fetchall()
    if result is not None:
        return [res[0] for res in result]


def bringProgramFromEducationPlan():
    db = MyDB('parametric')
    result = db.parametricQuery("SELECT program FROM actividades_de_formacion GROUP BY program").fetchall()
    if result is not None:
        return [res[0] for res in result]


def bringLineFromEducationPlan(program):
    db = MyDB('parametric')
    result = db.parametricQuery(
        "SELECT line FROM actividades_de_formacion WHERE program = '%s' GROUP BY line" % program).fetchall()
    if result is not None:
        return [res[0] for res in result]


def bringLevelFromEducationPlan(program, line):
    db = MyDB('parametric')
    result = db.parametricQuery(
        "SELECT level FROM actividades_de_formacion WHERE program = '%s' AND line = '%s' GROUP BY level" % (
            program, line)).fetchall()
    if result is not None:
        return [res[0] for res in result]


def bringDescriptionsFromEducationPlan(program, line, level):
    db = MyDB('parametric')
    result = db.parametricQuery(
        "SELECT description FROM actividades_de_formacion WHERE program = '%s' AND line = '%s' AND level = '%s'" % (
            program, line, level)).fetchall()
    if result is not None:
        return [res[0] for res in result]


def bringCIUU():
    db = MyDB('parametric')
    result = db.parametricQuery("SELECT id FROM ciiu").fetchall()
    if result is not None:
        return [str(res[0]) for res in result]


def traer_descripcion_actividad_formacion(id_actividad):
    db = MyDB('parametric')
    result = db.query("SELECT description FROM actividades_de_formacion WHERE id = :id_actividad",
                      {'id_actividad': id_actividad}).fetchone()
    if result is not None:
        return result[0]


def bringColumns(table):
    db = MyDB('register')
    result = db.parametricQuery("PRAGMA table_info(%s)" % table).fetchall()
    if result is not None:
        return [res[1] for res in result]


def lista_de_tablas():
    db = MyDB('register')
    result = db.parametricQuery("SELECT name FROM sqlite_master WHERE type = 'table' AND name NOT LIKE 'sqlite_%' AND "
                                "name NOT LIKE 'odp_%' AND name NOT LIKE 'proyectos'").fetchall()
    result = [res[0] for res in result]
    return result


def limpiar_tabla(tabla):
    db = MyDB('register')
    db.fast_commit("DELETE FROM %s" % tabla)

def obtener_toda_info(tabla):
    db = MyDB('register')
    result = db.parametricQuery("SELECT * FROM %s" % tabla).fetchall()
    return result
