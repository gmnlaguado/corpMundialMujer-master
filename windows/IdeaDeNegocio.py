# coding=utf-8
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from declarations import querys, class_declaration, dataFormating
from codes import snippets


class IdeaDeNegocioScreen(Screen):
    payeeDocument = None
    project = None
    operator = None
    productServicesList = None
    colaboratorsList = None

    id_entrepreneurship = ObjectProperty()
    id_bussinesSector = ObjectProperty()
    id_cities = ObjectProperty()
    id_studies = ObjectProperty()
    id_agricultural = ObjectProperty()
    id_needColabs = ObjectProperty()
    id_weeklyTime = ObjectProperty()
    id_whyNot = ObjectProperty()
    id_months = ObjectProperty()
    id_ciiu = ObjectProperty()
    id_howArise = ObjectProperty()
    id_haveExperience = ObjectProperty()
    id_departments = ObjectProperty()
    id_dedicationTime = ObjectProperty()
    id_productServices = ObjectProperty()
    id_briefcase = ObjectProperty()
    id_assetInvestment = ObjectProperty()
    id_investmentPercent = ObjectProperty()
    id_firstMonthSales = ObjectProperty()
    id_initialInvestment = ObjectProperty()
    id_capitalWorkInvestment = ObjectProperty()
    id_firstYearSales = ObjectProperty()
    id_imagine = ObjectProperty()
    id_message = ObjectProperty()
    id_signInButton = ObjectProperty()

    def on_pre_enter(self, *args):
        self.id_assetInvestment.input_type = 'number'
        self.id_firstYearSales.input_type = 'number'
        self.id_initialInvestment.input_type = 'number'
        self.id_firstMonthSales.input_type = 'number'

        self.id_briefcase.hint_text = "Portafolio"
        self.id_assetInvestment.hint_text = "Inv. Activos"
        self.id_firstMonthSales.hint_text = "Ventas primer mes"
        self.id_initialInvestment.hint_text = "Inv. Inicial"
        self.id_firstYearSales.hint_text = "Ventas Primer año"
        self.id_imagine.hint_text = "Imagine su negocio"

        self.id_bussinesSector.values = querys.parametricList('sector_empresarial')
        self.id_studies.values = querys.parametricList('si_no')
        self.id_agricultural.values = querys.parametricList('si_no')
        self.id_needColabs.values = querys.parametricList('si_no')
        self.id_weeklyTime.values = querys.parametricList('tiempo_semanal')
        self.id_whyNot.values = querys.parametricList('por_que_no')
        self.id_months.values = [str(numb) for numb in range(0, 70)]
        
        self.id_howArise.values = querys.parametricList('como_surge')
        self.id_haveExperience.values = querys.parametricList('si_no')
        self.id_departments.values = querys.bringDepartments(169)
        self.id_dedicationTime.values = querys.parametricList('tiempo_a_dedicar')
        self.id_productServices.values = querys.parametricList('producto_o_servicio')
        self.id_investmentPercent.values = querys.parametricList('porcentaje_de_inversion')

        self.id_departments.bind(text=self.fillCities)

        self.id_entrepreneurship.bind(on_text_validate=self.signal)
        self.id_briefcase.bind(on_text_validate=self.signal)
        self.id_firstMonthSales.bind(on_text_validate=self.capital_trabajo)
        self.id_initialInvestment.bind(on_text_validate=self.signal)
        self.id_assetInvestment.bind(on_text_validate=self.signal)
        self.id_firstYearSales.bind(on_text_validate=self.signal)
        self.id_imagine.bind(on_text_validate=self.signal)
        self.id_ciiu.bind(on_text_validate=self.signal)

        self.id_signInButton.bind(on_release=self.checkAll)

        self.id_bussinesSector.text = "Sector Empresarial"
        self.id_cities.text = "Ciudad"
        self.id_studies.text = "Estudios sobre el tema"
        self.id_agricultural.text = "¿Agropecuario?"
        self.id_needColabs.text = "Necesita colaboradores"
        self.id_weeklyTime.text = "Tiempo semanal a dedicar"
        self.id_whyNot.text = "¿Por qué no empezaba?"
        self.id_months.text = "Meses que lleva el negocio"
        self.id_howArise.text = "¿Cómo surge la idea?"
        self.id_haveExperience.text = "¿Experiencia?"
        self.id_departments.text = "Departamento"
        self.id_dedicationTime.text = "Tiempo a dedicar"
        self.id_productServices.text = "Producto / Servicio"
        self.id_investmentPercent.text = "% Inversión"
        self.id_message.text = ""
        self.id_signInButton.text = "Ingresar"

        self.id_entrepreneurship.resetInput()
        self.id_briefcase.resetInput()
        self.id_assetInvestment.resetInput()
        self.id_firstMonthSales.resetInput()
        self.id_initialInvestment.resetInput()
        self.id_capitalWorkInvestment.text = "Capital de trabajo"
        self.id_firstYearSales.resetInput()
        self.id_imagine.resetInput()

    def capital_trabajo(self, *args):
        self.signal(args[0])
        if self.id_message.text == "":
            activos = self.id_initialInvestment.text
            inicial = self.id_assetInvestment.text

            val_1 = activos.replace('.','')
            val_2 = inicial.replace('.','')

            valor = int(val_1) + int(val_2)
            self.id_capitalWorkInvestment.text = str(valor)

        
    def checkAll(self, *args):
        self.id_message.text = ""
        children_list = self.children[0].children
        ret = snippets.chekingCompletes(children_list)
        if not ret:
            msg = "Formulario Incompleto"
        else:
            msg = ""
        self.id_message.text = msg
        if msg == "":
            ProductServicesPopUp(self.operator, self.id_productServices.text, self.payeeDocument,
                                 self.id_needColabs.text).open()

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

    def on_leave(self, *args):
        information = self
        dataFormating.bussinesIdeaData(information)


class AcceptFormIdea(class_declaration.PopupFather):
    id_acceptButton = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.payeeDocument = args[0]
        self.id_acceptButton.bind(on_release=self.on_validate)

    def on_pre_open(self):
        self.title = f"ODP verifique que la información de {self.payeeDocument} es correcta antes de continuar"

    def on_validate(self, *args):
        self.dismiss()
        self.changeWindow()

    def changeWindow(self, *args):
        pass


class ProductServicesPopUp(class_declaration.PopupFather):
    id_list = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.operator = args[0]
        self.type = args[1]
        self.payeeDocument = args[2]
        self.needColabs = args[3]
        self.id_list.bind(on_text_validate=self.on_validate)

    def on_pre_open(self):
        self.title = f"ODP {self.operator} ingrese el listado de {self.type}s del beneficiario {self.payeeDocument}"

    def on_validate(self, *args):
        if self.id_list.alertFlag['complete']:
            self.dismiss()
            IdeaDeNegocioScreen.productServicesList = self.id_list.text
            if self.needColabs == "no":
                AcceptFormIdea(self.payeeDocument).open()
            else:
                colaboratorsPopUp(self.payeeDocument).open()
        else:
            class_declaration.MessagePopup(self.id_list.alertFlag['message']).open()


class colaboratorsPopUp(class_declaration.PopupFather):
    id_list = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.payeeDocument = args[0]
        self.id_list.bind(on_text_validate=self.on_validate)

    def on_pre_open(self):
        self.title = f"Ingrese los colaboradores necesarios para ejecutar la idea de {self.payeeDocument}"

    def on_validate(self, *args):
        if self.id_list.alertFlag['complete']:
            self.dismiss()
            IdeaDeNegocioScreen.colaboratorsList = self.id_list.text
            AcceptFormIdea(self.payeeDocument).open()
        else:
            class_declaration.MessagePopup(self.id_list.alertFlag['message']).open()