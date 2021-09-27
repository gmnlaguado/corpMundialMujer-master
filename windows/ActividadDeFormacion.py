# coding=utf-8
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from declarations import class_declaration, querys
import datetime
from windows import Monitoreo


class ActividadDeFormacionScreen(Screen):
    project = None
    operator = None
    payeeDocument = None
    home = False
    actividades = []
    actividades_realizadas = 0
    actividades_faltantes = 0

    id_title = ObjectProperty()
    id_payee = ObjectProperty()
    id_payeeDocument = ObjectProperty()
    id_done = ObjectProperty()
    id_pending = ObjectProperty()
    id_percentage = ObjectProperty()
    id_activities = ObjectProperty()
    id_message = ObjectProperty()
    id_signInButton = ObjectProperty()
    id_homeButton = ObjectProperty()

    def checkAll(self, *args):
        AcceptFormActividadDeFormacion(self.operator).open()

    def on_pre_enter(self, *args):
        self.id_title.text = "Actvidad de Formación"
        self.id_activities.bind(text=self.selectActivity)
        self.id_signInButton.bind(on_release=self.checkAll)

        self.id_activities.text = "Actividad De Formación"
        self.id_activities.values = self.actividades
        self.id_payee.text = f'Beneficiario {self.payeeDocument}'
        self.id_payeeDocument.text = f'Proyecto: {self.project}'
        self.id_done.text = f'A. realizadas {self.actividades_realizadas}'
        self.id_pending.text = f'A. faltantes {self.actividades_faltantes}'
        porcentaje = (self.actividades_realizadas/(self.actividades_faltantes + self.actividades_realizadas))*100
        self.id_percentage.text = f'Porcentaje {porcentaje:.1f}%'

    def selectActivity(self, *args):
        if args[1] != "Actividad De Formación":
            SeleccionarActividad(self.payeeDocument, querys.idProject(self.project.lower()), args[1], self.operator, self.actividades_faltantes).open()


class SeleccionarActividad(class_declaration.PopupFather):
    id_date = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.document = args[0]
        self.project = args[1]
        self.actividad = args[2]
        self.operator = args[3]
        self.faltantes = args[4]
        self.id_date.bind(on_release=self.on_validate)

    def on_pre_open(self):
        self.title = f"{self.operator} ¿Está seguro de registrar esta actividad?"

    def on_validate(self, *args):
        act = self.actividad.split(' ')[:-1]
        act = ' '.join(act)
        act = querys.traer_id_de_actividad_de_formacion(act)
        querys.dar_actividad_de_formacion_como_finalizada(self.document, self.project, act, str(datetime.date.today()))
        class_declaration.MessagePopup('La actividad ha sido registrada').open()
        if self.faltantes == 1:
            querys.registrar('beneficiario_proyectos', 'concluido_formacion', self.document, self.project, 1)
            querys.registrar('beneficiario_proyectos', 'etapa_del_proceso', self.document, self.project, 3)
            querys.registrar('beneficiario_proyectos', 'monitoreo', self.document, self.project, 1)
        self.changeWindow()
        self.dismiss()

    def changeWindow(self, *args):
        pass


class AcceptFormActividadDeFormacion(class_declaration.PopupFather):
    id_acceptButton = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.operator = args[0]
        self.id_acceptButton.bind(on_release=self.on_validate)

    def on_pre_open(self):
        self.title = f"ODP {self.operator} verifique que la información es correcta antes de continuar"

    def on_validate(self, *args):
        self.dismiss()
        self.changeWindow()

    def changeWindow(self, *args):
        pass