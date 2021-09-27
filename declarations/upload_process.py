# coding=utf-8
from declarations import querys
from kivy.network.urlrequest import UrlRequest
from codes import snippets
from kivy.clock import mainthread
import json


def get_operarios():
    url = 'http://190.145.94.93:5000/obtener_operarios'
    method = "POST"
    req_body = "req_body"
    req = UrlRequest(url, 
                    method = method, 
                    req_body = req_body, 
                    on_success=operarios_respuesta, 
                    on_progress=operarios_progreso)

def operarios_respuesta(*args):
    snippets.actualizando_operarios(args[1])

def operarios_progreso(*args):
    print('\t',args[0].resp_status)


def get_operarios_proyectos():
    url = 'http://190.145.94.93:5000/obtener_operarios_proyectos'
    method = "POST"
    req_body = "req_body"
    req = UrlRequest(url, 
                    method = method, 
                    req_body = req_body, 
                    on_success=operarios_respuesta_2, 
                    on_progress=operarios_progreso_2)

def operarios_respuesta_2(*args):
    snippets.actualizando_operarios_proyectos(args[1])

def operarios_progreso_2(*args):
    print('\t',args[0].resp_status)

