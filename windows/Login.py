# coding=utf-8
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from declarations import querys, class_declaration, upload_process
from windows import Panel, InformacionGeneral, IdeaDeNegocio, UnidadDeNegocio, \
    CaracterizacionAmpliada, Monitoreo, DiagnosticoEmpresarial, PlanDeFormacion, ActividadDeFormacion, \
    PlanDeImplementacion, ActividadDeImplementacion
from codes import snippets

class LoginScreen(Screen):
    id_username = ObjectProperty()
    static_password = ObjectProperty()
    id_password = ObjectProperty()
    id_message = ObjectProperty()
    id_signInButton = ObjectProperty()
    id_wifi = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)

        self.static_password.text = "Contraseña"

    def on_pre_enter(self, *args):
        self.elements = []
        self.elements.append(self.id_username)
        self.elements.append(self.id_password)

        self.id_username.bind(on_text_validate=self.signal)
        self.id_password.bind(on_text_validate=self.signal)
        self.id_signInButton.bind(on_release=self.checkAll)
        if snippets.verificando_wifi():
            self.id_wifi.background_normal = './images/wifi_si.png'
            upload_process.get_operarios()
            upload_process.get_operarios_proyectos()


    def signal(self, *args):
        self.id_message.text = args[0].alertFlag['message']

    def checkAll(self, *args):
        if False in [element.complete for element in self.elements]:
            self.id_message.text = "Ingrese los datos"
        else:
            op = querys.idOperator(self.id_username.text)
            if op is not None:
                upload_process.get_operarios()
                ps = querys.passwordOperator(op)
                if self.id_password.text == ps:
                    LoginProjectPopup(self.id_username.text, op).open()
                else:
                    self.id_message.text = "Contraseña no coincide"
            else:
                self.id_message.text = "ODP no existe"


class LoginProjectPopup(class_declaration.PopupFather):

    id_projects = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.operator = args[0]
        self.document = args[1]

    def on_pre_open(self):
        self.title = f"ODP consultor {self.operator} seleccione el proyecto en el que va a trabajar ahora"
        projects = [querys.nameProject(proj).capitalize() for proj in querys.projectsOperator(self.document)]
        self.id_projects.values = projects
        self.id_projects.bind(text=self.on_selection)

    def on_selection(self, *args):
        Panel.PanelScreen.operator = self.operator
        Panel.PanelScreen.project = args[1]

        InformacionGeneral.InformacionGeneralScreen.operator = self.operator
        InformacionGeneral.InformacionGeneralScreen.project = args[1]

        IdeaDeNegocio.IdeaDeNegocioScreen.operator = self.operator
        IdeaDeNegocio.IdeaDeNegocioScreen.project = args[1]

        UnidadDeNegocio.UnidadDeNegocioScreen.operator = self.operator
        UnidadDeNegocio.UnidadDeNegocioScreen.project = args[1]

        CaracterizacionAmpliada.CaracterizacionAmpliadaScreen.operator = self.operator
        CaracterizacionAmpliada.CaracterizacionAmpliadaScreen.project = args[1]

        Monitoreo.MonitoreoScreen.operator = self.operator
        Monitoreo.MonitoreoScreen.project = args[1]

        DiagnosticoEmpresarial.DiagnosticoEmpresarialScreen.operator = self.operator
        DiagnosticoEmpresarial.DiagnosticoEmpresarialScreen.project = args[1]

        PlanDeFormacion.PlanDeFormacionScreen.operator = self.operator
        PlanDeFormacion.PlanDeFormacionScreen.project = args[1]

        ActividadDeFormacion.ActividadDeFormacionScreen.operator = self.operator
        ActividadDeFormacion.ActividadDeFormacionScreen.project = args[1]

        PlanDeImplementacion.PlanDeImplementacionScreen.operator = self.operator
        PlanDeImplementacion.PlanDeImplementacionScreen.project = args[1]

        ActividadDeImplementacion.ActividadDeImplementacionScreen.operator = self.operator
        ActividadDeImplementacion.ActividadDeImplementacionScreen.project = args[1]

        self.dismiss()
        self.changeWindow()

    def changeWindow(self, *args):
        pass










