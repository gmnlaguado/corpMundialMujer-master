# coding=utf-8
from kivy.uix.button import Button
from declarations import checkings
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from declarations import querys


class BoxLayoutFull(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.class_type = "container"


class TextInputFather(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_name = "montserrat"
        self.size_hint = None, None
        self.halign = "center"
        self.valign = "middle"
        self.color = 0, 0, 0, 1
        self.background_color = 1, 1, 1, 1
        self.background_normal = ''
        self.multiline = False
        self.class_type = "input"
        self.complete = False
        self.text_type = "username"
        self.alert = ""

    @property
    def alertFlag(self):
        self.on_text_validate()
        return_value = {'message': self.alert, 'complete': self.complete}
        return return_value

    def on_text_validate(self, *args):
        self.alert = ""
        if self.text_type == "username":
            if checkings.username(self.text):
                self.complete = True
            else:
                self.alert = "Usuario Incorrecto"
                self.complete = False

        if self.text_type == "password":
            if checkings.password(self.text):
                self.complete = True
            else:
                self.alert = "Contraseña Incorrecta"
                self.complete = False

        if self.text_type == "date":
            if checkings.date(self.text):
                self.complete = True
            else:
                self.alert = "Formato de Fecha Incorrecto"
                self.complete = False

        if self.text_type == "name":
            if checkings.name(self.text):
                self.complete = True
            else:
                self.alert = "Nombre/Apellido Incorrecto"
                self.complete = False

        if self.text_type == "text":
            if checkings.text(self.text):
                self.complete = True
            else:
                self.alert = "Formato de texto Incorrecto"
                self.complete = False

        if self.text_type == "phone":
            if checkings.phone(self.text):
                self.complete = True
            else:
                self.alert = "Teléfono fijo Incorrecto"
                self.complete = False

        if self.text_type == "cellphone":
            if checkings.cellphone(self.text):
                self.complete = True
            else:
                self.alert = "Teléfono celular Incorrecto"
                self.complete = False

        if self.text_type == "money":
            if checkings.money(self.text):
                self.complete = True
            else:
                self.alert = "Formato de dinero Incorrecto"
                self.complete = False

        if self.text_type == "after_date":
            if checkings.after_date(self.text):
                self.complete = True
            else:
                self.alert = "Formato de fecha incorrecto"
                self.complete = False
        
        if self.text_type == "nit":
            if checkings.nit(self.text):
                self.complete = True
            else:
                self.alert = "Formato de NIT incorrecto"
                self.complete = False

        if self.text_type == "ciiu":
            ciius = querys.bringCIUU()
            ciius = ['0'+cii if len(cii) == 3 else cii for cii in ciius]
            if self.text in ciius:
                self.complete = True
            else: 
                self.alert = "Código CIIU no existe"
                self.complete = False

        if self.text_type == "nothing":
            if len(self.text) > 0:
                self.complete = True
            else:
                self.alert = "No se permiten campos vacios"
                self.complete = False

        if self.complete:
            self.background_color = 7 / 255, 7 / 255, 7 / 255, 0.1
        else:
            self.background_color = 1, 1, 1, 1

    def resetInput(self):
        self.background_color = 1, 1, 1, 1
        self.text = ""


class ButtonFather(Button):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.font_name = "montserrat"
        self.color = 1, 1, 1, 1
        self.size_hint = None, None
        self.halign = "center"
        self.valign = "middle"
        self.background_color = 39 / 255, 76 / 255, 0 / 255, 0.76
        self.background_normal = ''
        self.class_type = 'button'
        self.button_type = 1
        self.button_generated_text = ""

    def on_press(self):
        if self.button_type == 1:
            self.button_generated_text = "Verifique que todos los datos son correctos antes de continuar"

        if self.button_type == 2:
            self.button_generated_text = "Ingrese el número de documento del beneficiario para realizar " \
                                         "caracterización básica"
        if self.button_type == 3:
            self.button_generated_text = "Seleccione el beneficiario a inactivar, ¡Cuidado! Esto no podrá ser cambiado"


class HomeButtonFather(Button):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = './images/home.png'
        self.background_down = './images/home.png'
        self.size_hint = None, None
        self.size = 80, 80
        self.class_type = "button"


class SpinnerFather(Spinner):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.font_name = "montserrat"
        self.color = 1, 1, 1, 1
        self.size_hint = None, None
        self.halign = "center"
        self.valign = "middle"
        self.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
        self.complete = False
        self.class_type = "spinner"
        self.text_init = ['Proyectos', "Tipo de documento", "Depto. Expedición", "Ciudad Expedición", "Sexo", "Tipo",
                          "Nacionalidad", "País", "Departamento", "Ciudad", "Entorno", "Dirección", "Rótulo", "Barrio",
                          "Estrato", "Género", "Etnia", "Cond. Discapacidad", "Sector Empresarial",
                          "Estudios sobre el tema", "¿Agropecuario?", "Necesita colaboradores",
                          "Tiempo semanal a dedicar", "¿Por qué no empezaba?", "Meses que lleva el negocio", "CIIU",
                          "¿Cómo surge la idea?", "¿Experiencia?", "Tiempo a dedicar", "Producto / Servicio",
                          "% Inversión", "Si existe seleccione", "¿Cuantos socios?", "Sector empresarial",
                          "Reg. Cámara comercio", "Colab. con contrato", "Colab. sin contrato", 'Nivel de escolaridad',
                          '¿Tiene vinculación laboral con contrato?', '¿Independiente?', '¿Es cabeza de familia?', 
                          'Número de integrantes en el hogar', 'Régimen de salud', 'Estado Civil', 'Tipo de contrato',
                          '¿Tiene RUT?', '¿Número de hijos?', '¿Cuántas personas tiene a cargo?', '¿Cubre su familia?',
                          'Promedio de ingresos por contrato', 'Promedio de ingresos en esta actividad', 'Pensión', 'ARL',
                          "¿Es una asociación de mujeres?", "Material predominante", "Tipo de vivienda", "Antiguedad",
                          "Número de dormitorios", "Combustible usado en cocina", "Sujeto y fuentes de ingreso",
                          "Personas que dependen economicamente de usted", "¿Quién define la distribución de dinero en el hogar",
                          "Gastos y cantidad", "¿Pertenece a asociación", "¿Pertenece a alguna asociación?", 
                          "Total de personas que dependen de este ingreso", "¿Quién define la distribución de ingresos?",
                          "Material predominante de la vivienda", "Combustible de cocina", "Programa", "Linea", "Nivel",
                          "Actividad De Formación", 'Antiguedad del contrato', 'Tipo de seguimiento', 'Alerta', 'Cantidad de visitas']

    def on_text(self, *args):
        if args[1] not in self.text_init:
            self.background_color = 11 / 255, 69 / 255, 0 / 255, 0.7
            self.complete = True
        else:
            self.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
            self.complete = False


class PopupFather(Popup):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.background = "images/green_background.png"
        self.background_color = 1, 1, 1, 1
        self.separator_color = 0, 0, 0, 0
        self.font_name = "montserrat"
        self.title_align = "center"
        self.title_color = 0, 0, 0, 1
        self.size_hint = None, None


class MessagePopup(Popup):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.background = "images/green_background.png"
        self.background_color = 1, 1, 1, 1
        self.separator_color = 0, 0, 0, 0
        self.font_name = "montserrat"
        self.title_align = "center"
        self.title_color = 1, 0, 0, 1
        self.size_hint = None, None
        self.top = 800 - 232
        self.x = 357
        self.size = 566, 43 * 3
        self.title_size = 43
        self.title = args[0]

    def on_open(self):
        Clock.schedule_interval(self.dismissCall, 1)

    def dismissCall(self, dt):
        self.dismiss()


class Wifi_Status(Button):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = './images/wifi_no.png'
        self.background_down = './images/wifi_no.png'
        self.size_hint = None, None
        self.size = 30,25
        self.class_type = "button"
        self.top = 800-64
        self.x = 357.05
        self.conexion = False