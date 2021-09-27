# coding=utf-8
from datetime import date
import requests
from declarations import querys

def chekingCompletes(children_list):
    for idx, child in enumerate(children_list):
        if 'class_type' in dir(child):
            if child.class_type in ['spinner', 'input']:
                if not child.complete:
                    return False
            elif child.class_type == "container":
                for chil in child.children:
                    children_list.append(chil)
    return True


def ageCalculation(age):
    today = [int(integer) for integer in str(date.today()).split('-')[::-1]]
    data = [int(integer) for integer in age.split('/')]
    years = today[-1] - data[-1]
    if today[-2] == data[-2]:
        if today[-3] < data[-3]:
            years -= 1
    elif today[-2] < data[-2]:
        years -= 1
    return years


def rangeCalculation(age):
    if 15 <= age <= 19:
        return 1
    elif 20 <= age <= 29:
        return 2
    elif 30 <= age <= 39:
        return 3
    elif 40 <= age <= 49:
        return 4
    elif 50 <= age <= 59:
        return 5
    else:
        return 6


def formattingDate(datetime_date):
    datetime_date = '-'.join(datetime_date.split('/')[::-1])
    return datetime_date


def verificando_wifi(url='http://www.google.com/', timeout=3):
    try:
        r = requests.head(url, timeout=timeout)
        return True
    except requests.ConnectionError as ex:
        print(ex)
        return False


def actualizando_operarios(data):
    info = data[2:-2].decode("utf-8") 
    info = info.split("), (")
    operarios = []
    for inf in info:
        operario = []
        for data in inf.split(", "):
            operario.append(data[1:-1])
        operario.append(1)
        operarios.append(tuple(operario))

    querys.limpiar_tabla("odp_operario")
    for operario_info in operarios:
        querys.cargar('odp_operario', 5, operario_info)


def actualizando_operarios_proyectos(data):
    info = data[2:-2].decode("utf-8") 
    info = info.split("), (")
    operarios = []
    for inf in info:
        operario = []
        for data in inf.split(", "):
            operario.append(data[1:-1])
        operarios.append(tuple(operario))

    querys.limpiar_tabla("odp_operario_proyectos")
    for operario_info in operarios:
        querys.cargar('odp_operario_proyectos', 3, operario_info)