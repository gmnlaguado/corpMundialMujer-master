# coding=utf-8
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from declarations import querys, class_declaration, dataFormating
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from codes import snippets
from declarations import checkings


class MonitoreoScreen(Screen):
    project = None
    operator = None
    payeeDocument = None
    home = False
    # total_income_familiy = 0
    # total_gastos_familia = 0
    numero_de_monitoreo = 0

    id_belongToAssosiation = ObjectProperty()
    id_ciiu = ObjectProperty()
    id_pension = ObjectProperty()
    id_bussinesSector = ObjectProperty()
    id_householdExpenses = ObjectProperty()
    id_householdIncomes = ObjectProperty()
    id_totalDependants = ObjectProperty()
    id_whoDefineIncome = ObjectProperty()
    id_houseType = ObjectProperty()
    id_houseMaterial = ObjectProperty()
    id_bedroomsNumber = ObjectProperty()
    id_kitchenFuel = ObjectProperty()
    id_tier = ObjectProperty()
    id_houseAge = ObjectProperty()
    id_container_grid_1 = ObjectProperty()
    id_container_grid_2 = ObjectProperty()
    id_message = ObjectProperty()
    id_signInButton = ObjectProperty()
    id_homeButton = ObjectProperty()
    id_cual_asociacion = ObjectProperty()
    id_asociacion_mujeres = ObjectProperty()
    ingresos_familia = ObjectProperty()
    gastos_familia = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)



    def on_pre_enter(self, *args):

        self.id_belongToAssosiation.values = querys.parametricList('si_no')
        ciius = querys.bringCIUU()
        ciius = ['0' + cii if len(cii) == 3 else cii for cii in ciius]
        self.id_ciiu.values = ciius
        self.id_pension.values = querys.parametricList('si_no')
        self.id_bussinesSector.values = querys.parametricList('sector_empresarial')
        self.id_totalDependants.values = [str(numb) for numb in range(1, 30)]
        self.id_whoDefineIncome.values = querys.parametricList('quien_define_el_ingreso')
        self.id_houseType.values = querys.parametricList('tipo_de_casa')
        self.id_houseMaterial.values = querys.parametricList('material_de_la_casa')
        self.id_bedroomsNumber.values = [str(numb) for numb in range(0, 30)]
        self.id_kitchenFuel.values = querys.parametricList('combustible_de_cocina')
        self.id_tier.values = [str(numb) for numb in range(1, 8)]
        self.id_houseAge.values = querys.parametricList('antiguedad_de_la_casa')
        self.id_asociacion_mujeres.values = querys.parametricList('si_no')
        self.scroll_complete = False
        self.id_homeButton.bind(on_press=self.setHome)

        self.id_signInButton.bind(on_release=self.checkAll)
        self.id_belongToAssosiation.bind(text=self.pertenecer_asociacion)
        self.id_householdExpenses.bind(on_release=self.openPopupGastos)
        self.id_householdIncomes.bind(on_release=self.openPopupIngresos)
        self.id_ciiu.bind(on_text_validate=self.signal)

        if not len(self.id_container_grid_1.children) > 0:
            questions = querys.parametricList('caracteristicas_del_hogar')
            self.id_container_grid_1.bind(minimum_height=self.id_container_grid_1.setter('height'))
            for idx, quest in enumerate(questions):
                lab = Label(text=f'{idx + 1}]  ' + quest, halign="left", valign="middle", size_hint=(None, None),
                            size=(235, 18), color=(0, 0, 0, 0.85), font_size=14, font_name="montserrat",
                            text_size=(235, 18))
                box_container = BoxLayout()
                for i in ['Si', 'No']:
                    check = CheckBox(group=f"pregunta_{idx + 1}", color=(0, 1, 0, 1))
                    box_container.add_widget(check)
                self.id_container_grid_1.add_widget(lab)
                self.id_container_grid_1.add_widget(box_container)

        if not len(self.id_container_grid_2.children) > 0:
            self.id_container_grid_2.bind(minimum_height=self.id_container_grid_2.setter('height'))
            grid = SpinnerScroll(text="Cuenta corriente", values=querys.parametricList('si_no'))
            self.id_container_grid_2.add_widget(grid)

            self.id_container_grid_2.bind(minimum_height=self.id_container_grid_2.setter('height'))
            grid = SpinnerScroll(text="Cuenta de ahorros", values=querys.parametricList('si_no'))
            self.id_container_grid_2.add_widget(grid)

            grid = SpinnerScroll(text="Créditos", values=querys.parametricList('si_no'))
            self.id_container_grid_2.add_widget(grid)

            grid = SpinnerScroll(text="Pensiones", values=querys.parametricList('si_no'))
            self.id_container_grid_2.add_widget(grid)

            grid = SpinnerScroll(text="Seguros", values=querys.parametricList('si_no'))
            self.id_container_grid_2.add_widget(grid)

            box_container = BoxLayout(size_hint=(None, None), size=(673, 40))
            lab1 = Label(text="Monto del crédito", halign="left", valign="middle", size_hint=(None, None),
                         size=(275, 40), color=(0, 0, 0, 0.85), font_size=24, font_name="montserrat",
                         text_size=(275, 40))
            text1 = TextInputScroll()
            box_container.add_widget(lab1)
            box_container.add_widget(text1)
            self.id_container_grid_2.add_widget(box_container)

            grid = SpinnerScroll(text="Número de cuotas", values=[str(numb) for numb in range(1, 65)])
            self.id_container_grid_2.add_widget(grid)

            grid = SpinnerScroll(text="¿Alguno de estos servicios los tiene con Bancamía?",
                                 values=querys.parametricList('si_no'))
            self.id_container_grid_2.add_widget(grid)

            grid = SpinnerScroll(text="¿Cuál servicio tiene con Bancamía?", values=querys.parametricList('bancamia'))
            self.id_container_grid_2.add_widget(grid)

            grid_pertenece = SpinnerScroll(text="Pertenece a un programa público de desarrollo",
                                           values=querys.parametricList('si_no'))
            self.id_container_grid_2.add_widget(grid_pertenece)
            grid_pertenece.bind(text=self.ingresar_programa)

            box_container = BoxLayout(size_hint=(None, None), size=(673, 40))
            lab1 = Label(text="¿Cuál programa?", halign="left", valign="middle", size_hint=(None, None),
                         size=(275, 40), color=(0, 0, 0, 0.85), font_size=24, font_name="montserrat",
                         text_size=(275, 40))

            self.text_cual_programa = TextInputScroll()
            box_container.add_widget(lab1)
            box_container.add_widget(self.text_cual_programa)
            self.id_container_grid_2.add_widget(box_container)

            self.depende_de_alguien = SpinnerScroll(text="¿Depende económicamente de alguién?", values=querys.parametricList('si_no'))
            self.depende_de_alguien.bind(text=self.no_depende)
            self.id_container_grid_2.add_widget(self.depende_de_alguien)

            self.de_quien_depende_usted = SpinnerScroll(text="¿De quién depende?", values=querys.parametricList('de_quien_depende'))
            self.id_container_grid_2.add_widget(self.de_quien_depende_usted)

            grid = SpinnerScroll(text="¿Cuántas horas a la semana dedica al cuidado de personas a cargo?",
                                 values=[str(numb) for numb in range(0, 165)])
            self.id_container_grid_2.add_widget(grid)

            grid = SpinnerScroll(text="¿Cuántas horas a la semana dedica a la recreación?",
                                 values=[str(numb) for numb in range(0, 165)])
            self.id_container_grid_2.add_widget(grid)

            grid = SpinnerScroll(text="¿El negocio tiene RUT?", values=querys.parametricList('si_no'))
            self.id_container_grid_2.add_widget(grid)

            grid = SpinnerScroll(text="¿Tiene registro de cámara de comercio?", values=querys.parametricList('si_no'))
            self.id_container_grid_2.add_widget(grid)

            grid_tiene_nit = SpinnerScroll(text="¿Tiene NIT el negocio?", values=querys.parametricList('si_no'))
            self.id_container_grid_2.add_widget(grid_tiene_nit)
            grid_tiene_nit.bind(text=self.tiene_nit)

            box_container = BoxLayout(size_hint=(None, None), size=(673, 40))
            lab1 = Label(text="Número NIT", halign="left", valign="middle", size_hint=(None, None),
                         size=(275, 40), color=(0, 0, 0, 0.85), font_size=24, font_name="montserrat",
                         text_size=(275, 40))
            self.numero_nit = TextInputScroll()
            box_container.add_widget(lab1)
            box_container.add_widget(self.numero_nit)
            self.id_container_grid_2.add_widget(box_container)

            grid = SpinnerScroll(text="¿Dónde opera su unidad productivo?", values=querys.parametricList('donde_opera'))
            self.id_container_grid_2.add_widget(grid)

            input_list_labels = ["Ingreso del negocio", "Gastos Directos", "Gastos Indirectos", "Total de gastos",
                                 "Excedentes",
                                 "Activo Fijo", "Activo No Fijo", "Total Activos", "Pasivo Corto", "Pasivo Largo", "Deudas",
                                 "Patrimonio"]

            for input_label_value in input_list_labels:
                box_container = BoxLayout(size_hint=(None, None), size=(673, 40))
                lab1 = Label(text=input_label_value, halign="left", valign="middle", size_hint=(None, None),
                            size=(275, 40), color=(0, 0, 0, 0.85), font_size=24, font_name="montserrat",
                            text_size=(275, 40))
                text1 = TextInputScroll()

                if input_label_value == "Total Activos" or input_label_value == "Total de gastos":
                    text1.readonly = True

                if input_label_value == "Activo Fijo" or input_label_value == "Activo No Fijo":
                    text1.text_type = "money"
                    text1.bind(on_text_validate = self.sumando_activos)
                
                if input_label_value == "Gastos Directos" or input_label_value == "Gastos Indirectos":
                    text1.text_type = "money"
                    text1.bind(on_text_validate = self.total_gastos_suma)

                box_container.add_widget(lab1)
                box_container.add_widget(text1)
                self.id_container_grid_2.add_widget(box_container)

            self.total_workers = 0

            grid_trabajadores_con_contrato = SpinnerScroll(text="Total de trabajadores con contrato",
                                                           values=[str(numb) for numb in range(0, 60)])
            grid_trabajadores_con_contrato.bind(text=self.calc_workers)
            self.id_container_grid_2.add_widget(grid_trabajadores_con_contrato)

            grid_trabajadores_sin_contrato = SpinnerScroll(text="Total de trabajadores sin contrato",
                                                           values=[str(numb) for numb in range(0, 60)])
            grid_trabajadores_sin_contrato.bind(text=self.calc_workers)
            self.id_container_grid_2.add_widget(grid_trabajadores_sin_contrato)

            self.grid_label_workers = LabelScroll(text="Total de trabajadores")
            self.id_container_grid_2.add_widget(self.grid_label_workers)

            grid = SpinnerScroll(text="Cantidad de socios", values=[str(numb) for numb in range(0, 60)])
            self.id_container_grid_2.add_widget(grid)

            grid = SpinnerScroll(text="Tipo de local", values=querys.parametricList('tipo_de_casa'))
            self.id_container_grid_2.add_widget(grid)

        self.id_belongToAssosiation.text = "¿Pertenece a alguna asociación?"
        self.id_pension.text = "Pensión"
        self.id_bussinesSector.text = "Sector Empresarial"
        self.id_householdExpenses.text = "Gastos del grupo familiar"
        self.id_householdIncomes.text = "Fuente de ingresos del grupo familiar"
        self.id_totalDependants.text = "Total de personas que dependen de este ingreso"
        self.id_whoDefineIncome.text = "¿Quién define la distribución de ingresos?"
        self.id_houseType.text = "Tipo de vivienda"
        self.id_houseMaterial.text = "Material predominante de la vivienda"
        self.id_bedroomsNumber.text = "Número de dormitorios"
        self.id_kitchenFuel.text = "Combustible de cocina"
        self.id_tier.text = "Estrato"
        self.id_houseAge.text = "Antiguedad"
        self.id_asociacion_mujeres.text = "¿Es una asociación de mujeres?"
        self.scroll_complete = False
    
    def signal(self, *args):
        self.id_message.text = args[0].alertFlag['message']

    def no_depende(self, *args):
        if args[1] == "No":
            self.de_quien_depende_usted.text = "No Aplica"
            self.de_quien_depende_usted.complete = True
        elif args[1] == "Si":
            self.de_quien_depende_usted.complete = False
            self.de_quien_depende_usted.text = "¿De quién depende?"
            self.de_quien_depende_usted.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7

    def sumando_activos(self, *args):

        if len(self.id_container_grid_2.children[9].children[0].text) == 0:
            self.id_container_grid_2.children[9].children[0].text = args[0].text
        else:
            
            if checkings.money(args[0].text):

                val_1 = self.id_container_grid_2.children[9].children[0].text.replace('.','')
                val_2 = args[0].text.replace('.','')

                valor = int(val_1) + int(val_2)

                self.id_container_grid_2.children[9].children[0].text = str(valor)
            
        self.id_container_grid_2.children[9].children[0].complete = True
        self.id_container_grid_2.children[9].children[0].background_color = 20 / 255, 20 / 255, 20 / 255, 0.1

    def total_gastos_suma(self, *args):
        if len(self.id_container_grid_2.children[13].children[0].text) == 0:
            self.id_container_grid_2.children[13].children[0].text = args[0].text
        else:
            
            if checkings.money(args[0].text):

                val_1 = self.id_container_grid_2.children[13].children[0].text.replace('.','')
                val_2 = args[0].text.replace('.','')

                valor = int(val_1) + int(val_2)

                self.id_container_grid_2.children[13].children[0].text = str(valor)
                self.id_container_grid_2.children[12].children[0].text = self.total_excedentes()
                self.id_container_grid_2.children[12].children[0].complete = True
                self.id_container_grid_2.children[12].children[0].background_color = 20 / 255, 20 / 255, 20 / 255, 0.1
            
        self.id_container_grid_2.children[13].children[0].complete = True
        self.id_container_grid_2.children[13].children[0].background_color = 20 / 255, 20 / 255, 20 / 255, 0.1

        

    def total_excedentes(self, *args):
        ingresos = self.id_container_grid_2.children[16].children[0].text
        total_gastos = self.id_container_grid_2.children[13].children[0].text
        if len(ingresos) > 0 and len(total_gastos) > 0:
            ingresos = ingresos.replace('.','')
            total_gastos = total_gastos.replace('.','')
            excedentes = int(ingresos) - int(total_gastos)
            return str(excedentes)
        return str(0)



    def setHome(self, *args):
        self.home = True

    def ingresar_programa(self, *args):
        if args[1] == "No":
            self.text_cual_programa.complete = True
            self.text_cual_programa.text = "No Aplica"
            self.text_cual_programa.background_color = 7 / 255, 7 / 255, 7 / 255, 0.1
        elif args[1] == "Si":
            self.text_cual_programa.complete = False
            self.text_cual_programa.text = ""
            self.text_cual_programa.background_color = 255 / 255, 255 / 255, 255 / 255, 1

    def tiene_nit(self, *args):
        if args[1] == "No":
            self.numero_nit.text = "No Aplica"
            self.numero_nit.complete = True
            self.numero_nit.background_color = (7 / 255, 7 / 255, 7 / 255, 0.1)
        elif args[1] == "Si":
            self.numero_nit.text = ""
            self.numero_nit.complete = False
            self.numero_nit.background_color = (255 / 255, 255 / 255, 255 / 255, 1)

    def pertenecer_asociacion(self, *args):
        if args[1] == "No":
            self.id_cual_asociacion.text = "No Aplica"
            self.id_cual_asociacion.complete = True
            self.id_cual_asociacion.background_color = (7 / 255, 7 / 255, 7 / 255, 0.1)
            self.id_asociacion_mujeres.text = "No"
        elif args[1] == "Si":
            self.id_asociacion_mujeres.text = "¿Es una asociación de mujeres?"
            self.id_cual_asociacion.text = ""
            self.id_cual_asociacion.complete = False
            self.id_cual_asociacion.background_color = (255 / 255, 255 / 255, 255 / 255, 1)

    def calc_workers(self, *args):
        if args[1] != "Total de trabajadores con contrato" or args[1] != "Total de trabajadores sin contrato":
            self.total_workers += int(args[1])
            self.grid_label_workers.text = f'Cantidad total de trabajadores: {self.total_workers}'

    def checkAll(self, *args):
        self.id_message.text = ""
        for grid in self.id_container_grid_1.children:
            if len(grid.children) > 0 and not True in [box.active for box in grid.children]:
                self.id_message.text = "Faltan preguntas por responder"

        lista_spinners = []
        lista_texts = []
        items_scroll = self.id_container_grid_2.children
        for item in items_scroll[::-1]:
            if len(item.children) > 0:
                lista_texts.append(item.children[0].complete)
            try:
                if item.class_type == "spinner":
                    lista_spinners.append(item.complete)
            except AttributeError:
                pass

        if False in lista_spinners or False in lista_texts:
            self.scroll_complete = False
        else:
            self.scroll_complete = True

        if not self.scroll_complete:
            self.id_message.text = "Faltan todavía preguntas por responder"

        if self.ingresos_familia == "":
            self.id_message.text = "Faltan los ingresos familiares"

        if self.gastos_familia == "":
            self.id_message.text = "Faltan los gastos familiares"

        if self.id_message.text == "":
            children_list = self.children[0].children
            ret = snippets.chekingCompletes(children_list)
            if not ret:
                msg = "Formulario Incompleto"
            else:
                msg = ""
            self.id_message.text = msg
            if msg == "":
                AcceptFormMonitoreo(self.operator).open()



    def openPopupGastos(self, *args):
        GastosDelGrupoFamiliarPopup().open()

    def openPopupIngresos(self, *args):
        IngresosDelGrupoFamiliarPopup().open()

    def on_leave(self, *args):
        if not self.home:
            dataFormating.monitoreo(self)


class TextInputScroll(TextInput):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.size = (352, 40)
        self.font_name = "montserrat"
        self.color = (1, 1, 1, 1)
        self.size_hint = (None, None)
        self.halign = "center"
        self.valign = "middle"
        self.background_color = (255 / 255, 255 / 255, 255 / 255, 1)
        self.background_normal = ""
        self.complete = False
        self.class_type = "input"
        self.multiline = False
        self.readonly = False
        self.text_type = "Nada"

    def on_text_validate(self, *args):
        if self.text_type == "money":
            if checkings.money(self.text):
                self.complete = True
                self.background_color = 7 / 255, 7 / 255, 7 / 255, 0.1
            else:
                self.alert = "Formato de dinero Incorrecto"
                self.complete = False
                self.background_color = 1, 1, 1, 1
        else:
            self.complete = True
            self.background_color = 7 / 255, 7 / 255, 7 / 255, 0.1


class SpinnerScroll(Spinner):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.size = (673, 40)
        self.font_name = "montserrat"
        self.color = (1, 1, 1, 1)
        self.size_hint = (None, None)
        self.halign = "center"
        self.valign = "middle"
        self.background_color = (61 / 255, 119 / 255, 0 / 255, 0.7)
        self.background_normal = ""
        self.complete = False
        self.class_type = "spinner"

    def on_text(self, *args):
        self.background_color = 11 / 255, 69 / 255, 0 / 255, 0.7
        self.complete = True


class LabelScroll(Label):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.size = (673, 40)
        self.font_name = "montserrat"
        self.color = (0, 0, 0, 1)
        self.size_hint = (None, None)
        self.halign = "center"
        self.valign = "middle"
        self.class_type = "label"


class GastosDelGrupoFamiliarPopup(class_declaration.PopupFather):
    id_rentAndServices = ObjectProperty()
    id_runningCosts = ObjectProperty()
    id_education = ObjectProperty()
    id_casualCosts = ObjectProperty()
    id_obligations = ObjectProperty()
    id_message = ObjectProperty()
    id_acceptButton = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.title = f"Gastos del grupo familiar"
        self.id_acceptButton.bind(on_release=self.on_validate)

    def on_validate(self, *args):
        if self.id_rentAndServices.complete and self.id_runningCosts.complete and self.id_education.complete and self.id_casualCosts.complete and self.id_obligations.complete:
            
            self.id_rentAndServices.text = self.id_rentAndServices.text.replace('.','')
            self.id_runningCosts.text = self.id_runningCosts.text.replace('.','')
            self.id_education.text = self.id_education.text.replace('.','')
            self.id_casualCosts.text = self.id_casualCosts.text.replace('.','')
            self.id_obligations.text = self.id_obligations.text.replace('.','')

            total_expenses = int(self.id_rentAndServices.text) + int(self.id_runningCosts.text) + int(
                self.id_education.text) + int(self.id_casualCosts.text) + int(self.id_obligations.text)
            MonitoreoScreen.gastos_familia = str(total_expenses)
            # class_declaration.MessagePopup(f'Total gastos del grupo: {total_expenses}').open()
            self.dismiss()


class IngresosDelGrupoFamiliarPopup(class_declaration.PopupFather):
    id_employees = ObjectProperty()
    id_othersRelatives = ObjectProperty()
    id_freelanceJobs = ObjectProperty()
    id_pension = ObjectProperty()
    id_entrepreneurship = ObjectProperty()
    id_otherIncomes = ObjectProperty()
    id_message = ObjectProperty()
    id_acceptButton = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.title = f"Ingresos del grupo familiar"
        self.id_acceptButton.bind(on_release=self.on_validate)

    def on_validate(self, *args):
        if self.id_employees.complete and self.id_othersRelatives.complete and self.id_freelanceJobs.complete and self.id_pension.complete and self.id_entrepreneurship.complete and self.id_otherIncomes.complete:
            
            self.id_employees.text = self.id_employees.text.replace('.','')
            self.id_othersRelatives.text = self.id_othersRelatives.text.replace('.','')
            self.id_freelanceJobs.text = self.id_freelanceJobs.text.replace('.','')
            self.id_pension.text = self.id_pension.text.replace('.','')
            self.id_entrepreneurship.text = self.id_entrepreneurship.text.replace('.','')
            self.id_otherIncomes.text = self.id_otherIncomes.text.replace('.','')
            
            total_expenses = int(self.id_employees.text) + int(self.id_othersRelatives.text) + int(self.id_freelanceJobs.text) + int(self.id_pension.text) + int(self.id_entrepreneurship.text) + int(self.id_otherIncomes.text)
            MonitoreoScreen.ingresos_familia = str(total_expenses)
            # class_declaration.MessagePopup(f'Total ingresos del grupo: {total_expenses}').open()
            self.dismiss()


class AcceptFormMonitoreo(class_declaration.PopupFather):
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