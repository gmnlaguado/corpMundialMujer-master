# coding=utf-8
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from declarations import querys, class_declaration, dataFormating
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from codes import snippets
from windows import Monitoreo, UnidadDeNegocio


class CaracterizacionAmpliadaScreen(Screen):
    project = None
    operator = None
    payeeDocument = None
    home = False
    listado_hijos = False
    listado_cargo = False
    informacion_hijos = None
    informacion_personas_a_cargo = None

    id_title = ObjectProperty()
    id_adittionalStudies = ObjectProperty()
    id_studies = ObjectProperty()
    id_workingRelationship = ObjectProperty()
    id_freelance = ObjectProperty()
    id_householdHead = ObjectProperty()
    id_householdMembers = ObjectProperty()
    id_healthRegime = ObjectProperty()
    id_maritalStatus = ObjectProperty()
    id_agreementType = ObjectProperty()
    id_rut = ObjectProperty()
    id_childrenNumber = ObjectProperty()
    id_dependants = ObjectProperty()
    id_coverTheFamily = ObjectProperty()
    id_agreementTime = ObjectProperty()
    id_averageIncomeContract = ObjectProperty()
    id_averageIncomeActivity = ObjectProperty()
    id_childrenInformation = ObjectProperty()
    id_dependantsInformation = ObjectProperty()
    id_pension = ObjectProperty()
    id_arl = ObjectProperty()
    id_factorsThatPreventYou = ObjectProperty()
    id_observations = ObjectProperty()
    id_message = ObjectProperty()
    id_signInButton = ObjectProperty()
    id_homeButton = ObjectProperty()

    def on_pre_enter(self, *args):
        self.id_title.text = "Caracterización Ampliada"
        self.id_adittionalStudies.hint_text = "Formación superior o cursos complementarios"
        self.id_factorsThatPreventYou.hint_text = "Factores que le impiden participar en este proyecto"
        self.id_observations.hint_text = "Observaciones / aclaraciones"

        self.id_studies.values = querys.parametricList('estudios')
        self.id_workingRelationship.values = querys.parametricList('si_no')
        self.id_freelance.values = querys.parametricList('si_no')
        self.id_householdHead.values = querys.parametricList('si_no')
        self.id_healthRegime.values = querys.parametricList('regimen_de_salud')
        self.id_maritalStatus.values = querys.parametricList('estado_civil')
        self.id_agreementType.values = querys.parametricList('tipos_de_contrato')
        self.id_rut.values = querys.parametricList('si_no')
        self.id_childrenNumber.values = [str(numb) for numb in range(0, 30)]
        self.id_dependants.values = [str(numb) for numb in range(0, 30)]
        self.id_coverTheFamily.values = querys.parametricList('si_no')
        self.id_averageIncomeContract.values = querys.parametricList('promedio_de_ingresos')
        self.id_averageIncomeActivity.values = querys.parametricList('promedio_de_ingresos')
        self.id_pension.values = querys.parametricList('si_no')
        self.id_arl.values = querys.parametricList('si_no')
        self.id_householdMembers.values = [str(numb) for numb in range(1, 30)]
        self.id_agreementTime.values = [str(numb) for numb in range(0, 30)]

        self.id_homeButton.bind(on_press=self.setHome)

        self.id_signInButton.bind(on_release=self.checkAll)
        self.id_childrenInformation.bind(on_release=self.childrenInformation)
        self.id_dependantsInformation.bind(on_release=self.dependantsInformation)

        self.id_studies.text = 'Nivel de escolaridad'
        self.id_workingRelationship.text = '¿Tiene vinculación laboral con contrato?'
        self.id_freelance.text = '¿Independiente?'
        self.id_householdHead.text = '¿Es cabeza de familia?'
        self.id_householdMembers.text = 'Número de integrantes en el hogar'
        self.id_healthRegime.text = 'Régimen de salud'
        self.id_maritalStatus.text = 'Estado Civil'
        self.id_agreementType.text = 'Tipo de contrato'
        self.id_rut.text = '¿Tiene RUT?'
        self.id_childrenNumber.text = '¿Número de hijos?'
        self.id_dependants.text = '¿Cuántas personas tiene a cargo?'
        self.id_coverTheFamily.text = '¿Cubre su familia?'
        self.id_averageIncomeContract.text = 'Promedio de ingresos por contrato'
        self.id_averageIncomeActivity.text = 'Promedio de ingresos en esta actividad'
        self.id_childrenInformation.text = 'Información de hijos'
        self.id_dependantsInformation.text = 'Info. personas a cargo'
        self.id_pension.text = 'Pensión'
        self.id_arl.text = 'ARL'
        self.id_message.text = ''
        self.id_signInButton.text = 'Ingresar'
        self.id_agreementTime.text = 'Antiguedad del contrato'

        self.id_observations.resetInput()
        self.id_factorsThatPreventYou.resetInput()
        self.id_adittionalStudies.resetInput()

        self.id_workingRelationship.bind(text=self.no_vincula_laboralmente)
        self.id_freelance.bind(text=self.es_independiente)

        self.home = False

    def no_vincula_laboralmente(self, *args):
        if args[1] == "No":
            self.id_agreementType.text = "No Aplica"
            self.id_averageIncomeContract.text = "No Aplica"
            self.id_agreementTime.text = "0"
        else:
            self.id_agreementType.text = 'Tipo de contrato'
            self.id_averageIncomeContract.text = 'Promedio de ingresos por contrato'
            self.id_agreementTime.text = 'Antiguedad del contrato'

    def es_independiente(self, *args):
        if args[1] == "No":
            self.id_rut.text = "No"
            self.id_averageIncomeActivity.text = "No Aplica"
        else: 
            self.id_rut.text = '¿Tiene RUT?'
            self.id_averageIncomeActivity.text = 'Promedio de ingresos en esta actividad'

    def setHome(self, *args):
        self.home = True

    def childrenInformation(self, *args):
        if self.id_childrenNumber.text == '¿Número de hijos?':
            pass
        else:
            if self.id_childrenNumber.text != "0":
                InformacionHijos(int(self.id_childrenNumber.text)).open()

    def dependantsInformation(self, *args):
        if self.id_dependants.text == '¿Cuántas personas tiene a cargo?':
            pass
        else:
            if self.id_dependants.text != "0":
                InformacionPersonasACargo(int(self.id_dependants.text)).open()

    def checkAll(self, *args):
        self.id_message.text = ""

        if len(self.id_observations.text) == 0:
            self.id_observations.text = 'Sin observaciones'
            self.id_observations.on_text_validate()

        if len(self.id_factorsThatPreventYou.text) == 0:
            self.id_factorsThatPreventYou.text = 'Ninguno'
            self.id_factorsThatPreventYou.on_text_validate()

        if self.id_childrenNumber.text == "0":
            self.listado_hijos = True
        if self.id_dependants.text == "0":
            self.listado_cargo = True

        if self.listado_hijos and self.listado_cargo:
            children_list = self.children[0].children
            ret = snippets.chekingCompletes(children_list)
            if not ret:
                msg = "Formulario Incompleto"
            else:
                msg = ""
            self.id_message.text = msg
            if msg == "":
                AcceptFormCaracterizacionAmpliada(self.operator, self.payeeDocument).open()
        else:
            self.id_message.text = "Falta información por llenar"

    def on_leave(self, *args):
        informacion_limpia_hijos = []
        informacion_limpia_personas = []
        if not self.home:
            information = self
            if self.informacion_hijos is not None:
                for info in self.informacion_hijos:
                    try:
                        if info.class_type == "spinner":
                            informacion_limpia_hijos.append(info.text)
                    except AttributeError:
                        pass
            if self.informacion_personas_a_cargo is not None:
                for info in self.informacion_personas_a_cargo:
                    try:
                        if info.class_type == "spinner":
                            informacion_limpia_personas.append(info.text)
                    except AttributeError:
                        pass
            Monitoreo.MonitoreoScreen.payeeDocument = self.payeeDocument
            Monitoreo.MonitoreoScreen.numero_de_monitoreo = 1
            dataFormating.caracterizacion_ampliada_informacion_hijos(informacion_limpia_hijos, information)
            dataFormating.caracterizacion_ampliada_informacion_personas_a_cargo(informacion_limpia_personas, information)
            dataFormating.caracterizacion_ampliada(information)


class AcceptFormCaracterizacionAmpliada(class_declaration.PopupFather):
    id_acceptButton = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.operator = args[0]
        self.payee = args[1]
        self.id_acceptButton.bind(on_release=self.on_validate)

    def on_pre_open(self):
        self.title = f"ODP {self.operator} verifique que la información es correcta antes de continuar"

    def on_validate(self, *args):
        self.dismiss()
        if querys.tipo_de_beneficiario(self.payee) == 1:
            UnidadDeNegocio.UnidadDeNegocioScreen.caracterizacion_ampliada = True
            self.changeToUnidad()
        else:
            self.changeWindow()

    def changeWindow(self, *args):
        pass

    def changeToUnidad(self, *args):
        pass


class InformacionHijos(class_declaration.PopupFather):
    id_container_grid = ObjectProperty()
    id_botonAceptar = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.cantidad = args[0]

    def on_open(self):
        self.id_botonAceptar.bind(on_release=self.accionAceptar)
        self.id_container_grid.rows = int(self.cantidad) + 1
        self.title = "Información sobre hijos e hijas"
        self.id_container_grid.bind(minimum_height=self.id_container_grid.setter('height'))

        lab_1 = Label(text='Hijo', halign="center", valign="middle", size_hint=(None, None),
                      size=(40, 40), color=(0, 0, 0, 0.85), font_size=20, font_name="montserrat",
                      text_size=(40, 40))
        lab_2 = Label(text='Género', halign="center", valign="middle", size_hint=(None, None),
                      size=(318, 40), color=(0, 0, 0, 0.85), font_size=20, font_name="montserrat",
                      text_size=(318, 40))
        lab_3 = Label(text='Mayor de edad', halign="center", valign="middle", size_hint=(None, None),
                      size=(318, 40), color=(0, 0, 0, 0.85), font_size=20, font_name="montserrat",
                      text_size=(318, 40))
        lab_4 = Label(text='Cond. Discapacidad', halign="center", valign="middle", size_hint=(None, None),
                      size=(318, 40), color=(0, 0, 0, 0.85), font_size=20, font_name="montserrat",
                      text_size=(318, 40))

        self.id_container_grid.add_widget(lab_1)
        self.id_container_grid.add_widget(lab_2)
        self.id_container_grid.add_widget(lab_3)
        self.id_container_grid.add_widget(lab_4)

        for idx in range(int(self.cantidad)):
            lab = Label(text=str(idx + 1), halign="center", valign="middle", size_hint=(None, None),
                        size=(77, 40), color=(0, 0, 0, 0.85), font_size=20, font_name="montserrat",
                        text_size=(77, 40))
            spin_gen = SpinnerScroll(text='Género', values=querys.parametricList('genero'))
            spin_mayor = SpinnerScroll(text='Mayoría', values=querys.parametricList('si_no'))
            spin_disc = SpinnerScroll(text='Discapacidad', values=querys.parametricList('discapacidades'))

            self.id_container_grid.add_widget(lab)
            self.id_container_grid.add_widget(spin_gen)
            self.id_container_grid.add_widget(spin_mayor)
            self.id_container_grid.add_widget(spin_disc)

    def accionAceptar(self, *args):
        res = []
        for idx, childs in enumerate(self.id_container_grid.children):
            if idx < len(self.id_container_grid.children) - 4:
                res.append(childs.text)
        res = res[::-1]
        CaracterizacionAmpliadaScreen.hijosACargo = res
        if 'Género' in res or 'Mayoría' in res or 'Discapacidad' in res:
            pass
        else:
            CaracterizacionAmpliadaScreen.informacion_hijos = self.id_container_grid.children
            CaracterizacionAmpliadaScreen.listado_hijos = True
            self.dismiss()


class SpinnerScroll(Spinner):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = "images/dropdown_scroll.png"
        self.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
        self.halign = "center"
        self.valign = "middle"
        self.size_hint = (None, None)
        self.size = (318, 40)
        self.color = (1, 1, 1, 1)
        self.font_size = 20
        self.font_name = "montserrat"
        self.text_size = (318, 40)
        self.diligenciado = False
        self.id = 'Spinner'
        self.class_type = "spinner"

    def on_text(self, *args):
        self.background_color = 11 / 255, 69 / 255, 0 / 255, 0.7
        self.diligenciado = True


class InformacionPersonasACargo(class_declaration.PopupFather):
    id_container_grid = ObjectProperty()
    id_botonAceptar = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.cantidad = args[0]
        self.id_botonAceptar.bind(on_release=self.accionAceptar)

    def on_open(self):
        self.id_container_grid.rows = int(self.cantidad) + 1
        self.title = "Información sobre las personas que tiene a cargo"
        self.id_container_grid.bind(minimum_height=self.id_container_grid.setter('height'))

        lab_1 = Label(text='#', halign="center", valign="middle", size_hint=(None, None),
                      size=(40, 40), color=(0, 0, 0, 0.85), font_size=20, font_name="montserrat",
                      text_size=(40, 40))
        lab_2 = Label(text='Género', halign="center", valign="middle", size_hint=(None, None),
                      size=(318, 40), color=(0, 0, 0, 0.85), font_size=20, font_name="montserrat",
                      text_size=(318, 40))
        lab_3 = Label(text='Mayor de edad', halign="center", valign="middle", size_hint=(None, None),
                      size=(318, 40), color=(0, 0, 0, 0.85), font_size=20, font_name="montserrat",
                      text_size=(318, 40))
        lab_4 = Label(text='Cond. Discapacidad', halign="center", valign="middle", size_hint=(None, None),
                      size=(318, 40), color=(0, 0, 0, 0.85), font_size=20, font_name="montserrat",
                      text_size=(318, 40))

        self.id_container_grid.add_widget(lab_1)
        self.id_container_grid.add_widget(lab_2)
        self.id_container_grid.add_widget(lab_3)
        self.id_container_grid.add_widget(lab_4)

        for idx in range(int(self.cantidad)):
            lab = Label(text=str(idx + 1), halign="center", valign="middle", size_hint=(None, None),
                        size=(77, 40), color=(0, 0, 0, 0.85), font_size=20, font_name="montserrat",
                        text_size=(77, 40))
            spin_gen = SpinnerScroll(text='Género', values=querys.parametricList('genero'))
            spin_mayor = SpinnerScroll(text='Mayoría', values=querys.parametricList('si_no'))
            spin_disc = SpinnerScroll(text='Discapacidad', values=querys.parametricList('discapacidades'))

            self.id_container_grid.add_widget(lab)
            self.id_container_grid.add_widget(spin_gen)
            self.id_container_grid.add_widget(spin_mayor)
            self.id_container_grid.add_widget(spin_disc)

    def accionAceptar(self, *args):
        res = []
        for idx, childs in enumerate(self.id_container_grid.children):
            if idx < len(self.id_container_grid.children) - 4:
                res.append(childs.text)
        res = res[::-1]
        CaracterizacionAmpliadaScreen.personasACargo = res
        if 'Género' in res or 'Mayoría' in res or 'Discapacidad' in res:
            pass
        else:
            CaracterizacionAmpliadaScreen.informacion_personas_a_cargo = self.id_container_grid.children
            CaracterizacionAmpliadaScreen.listado_cargo = True
            self.dismiss()
