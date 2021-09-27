# coding=utf-8
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from declarations import querys, class_declaration, dataFormating
from codes import snippets


class UnidadDeNegocioScreen(Screen):
    payeeDocument = None
    project = None
    operator = None
    caracterizacion_ampliada = False

    id_unit = ObjectProperty()
    id_howManyPartners = ObjectProperty()
    id_ciiu = ObjectProperty()
    id_email = ObjectProperty()
    id_webPage = ObjectProperty()
    id_sector = ObjectProperty()
    id_regCamara = ObjectProperty()
    id_withContract = ObjectProperty()
    id_withoutContract = ObjectProperty()
    id_departments = ObjectProperty()
    id_cities = ObjectProperty()
    id_address = ObjectProperty()
    id_phone = ObjectProperty()
    id_cellphone = ObjectProperty()
    id_sign = ObjectProperty()
    id_tier = ObjectProperty()
    id_cellphone2 = ObjectProperty()
    id_descriptionLabel = ObjectProperty()
    id_description = ObjectProperty()
    id_briefcase = ObjectProperty()
    id_creationLabel = ObjectProperty()
    id_creation = ObjectProperty()
    id_nit = ObjectProperty()
    id_liabilitiesDescriptionLabel = ObjectProperty()
    id_liabilitiesDescription = ObjectProperty()
    id_message = ObjectProperty()
    id_signInButton = ObjectProperty()

    def on_pre_enter(self, *args):
        self.id_phone.input_type = 'number'
        self.id_cellphone.input_type = 'number'
        self.id_cellphone2.input_type = 'number'

        self.id_howManyPartners.text = "¿Cuantos socios?"
        self.id_sector.text = "Sector empresarial"
        self.id_regCamara.text = "Reg. Cámara comercio"
        self.id_withContract.text = "Colab. con contrato"
        self.id_withoutContract.text = "Colab. sin contrato"
        self.id_departments.text = "Departamento"
        self.id_cities.text = "Ciudad"
        self.id_sign.text = "Rótulo"
        self.id_tier.text = "Indicativo"
        self.id_descriptionLabel.text = "Descripción"
        self.id_creationLabel.text = "Creación"
        self.id_liabilitiesDescriptionLabel.text = "Descripción pasivos"
        self.id_signInButton.text = "Ingresar"

        self.id_unit.hint_text = "Nombre de la unidad de negocio"
        self.id_email.hint_text = "Email"
        self.id_webPage.hint_text = "Página Web"
        self.id_phone.hint_text = "Tel. Fijo"
        self.id_cellphone.hint_text = "Tel. Celular 1"
        self.id_cellphone2.hint_text = "Tel. Celular 2"
        self.id_description.hint_text = "Descripción de Unidad"
        self.id_briefcase.hint_text = "Portafolio"
        self.id_liabilitiesDescription.hint_text = "Descripción de pasivos"

        self.id_howManyPartners.values = [str(numb) for numb in range(0, 70)]
        ciius = querys.bringCIUU()
        ciius = ['0' + cii if len(cii) == 3 else cii for cii in ciius]
        self.id_ciiu.values = ciius
        self.id_sector.values = querys.parametricList('sector_empresarial')
        self.id_regCamara.values = querys.parametricList('si_no')
        self.id_withContract.values = [str(numb) for numb in range(0, 70)]
        self.id_withoutContract.values = [str(numb) for numb in range(0, 70)]
        self.id_departments.values = querys.bringDepartments(169)
        self.id_sign.values = querys.parametricList('rotulos')
        self.id_tier.values = [str(numb) for numb in range(1, 8)]

        self.id_departments.bind(text=self.fillCities)

        self.id_unit.bind(on_text_validate=self.signal)
        self.id_email.bind(on_text_validate=self.signal)
        self.id_webPage.bind(on_text_validate=self.signal)
        self.id_address.bind(on_text_validate=self.signal)
        self.id_phone.bind(on_text_validate=self.signal)
        self.id_cellphone.bind(on_text_validate=self.signal)
        self.id_cellphone2.bind(on_text_validate=self.signal)
        self.id_description.bind(on_text_validate=self.signal)
        self.id_briefcase.bind(on_text_validate=self.signal)
        self.id_creation.bind(on_text_validate=self.signal)
        self.id_nit.bind(on_text_validate=self.signal)
        self.id_ciiu.bind(on_text_validate=self.signal)
        self.id_liabilitiesDescription.bind(on_text_validate=self.signal)
        self.id_signInButton.bind(on_release=self.checkAll)

        self.id_unit.resetInput()
        self.id_email.resetInput()
        self.id_webPage.resetInput()
        self.id_address.resetInput()
        self.id_phone.resetInput()
        self.id_cellphone.resetInput()
        self.id_cellphone2.resetInput()
        self.id_description.resetInput()
        self.id_briefcase.resetInput()
        self.id_creation.resetInput()
        self.id_nit.resetInput()
        self.id_liabilitiesDescription.resetInput()

    def signal(self, *args):
        self.id_message.text = args[0].alertFlag['message']

    def fillCities(self, *args):
        self.id_message.text = ""
        id_department = querys.idDepartments(args[1])
        if id_department is not None:
            if id_department == 11:
                self.id_cities.text = args[1]
            else:
                self.id_cities.values = querys.bringCities(id_department)

    def checkAll(self, *args):
        self.id_message.text = ""

        if len(self.id_cellphone2.text) == 0:
            self.id_cellphone2.text = '0000000000'
            self.id_cellphone2.on_text_validate()

        if len(self.id_email.text) == 0:
            self.id_email.text = 'No Aplica'
            self.id_email.on_text_validate()

        if len(self.id_webPage.text) == 0:
            self.id_webPage.text = 'No Aplica'
            self.id_webPage.on_text_validate()
        
        if len(self.id_phone.text) == 0:
            self.id_phone.text = '0000000'
            self.id_phone.on_text_validate()

        children_list = self.children[0].children
        ret = snippets.chekingCompletes(children_list)
        if not ret:
            msg = "Formulario Incompleto"
        else:
            msg = ""
        self.id_message.text = msg
        if msg == "":
            AcceptFormUnit(self.operator).open()

    def on_leave(self, *args):
        information = self
        dataFormating.bussinesUnitData(information)


class AcceptFormUnit(class_declaration.PopupFather):
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
        if UnidadDeNegocioScreen.caracterizacion_ampliada:
            self.changeToMonitoreo()
        else:
            self.changeWindow()

    def changeWindow(self, *args):
        pass

    def changeToMonitoreo(self, *args):
        pass