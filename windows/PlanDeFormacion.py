# coding=utf-8
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from declarations import querys, class_declaration, checkings, dataFormating
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout


class PlanDeFormacionScreen(Screen):
    project = None
    operator = None
    payeeDocument = None
    home = False

    id_selectedActivities = ObjectProperty()
    id_program = ObjectProperty()
    id_line = ObjectProperty()
    id_level = ObjectProperty()
    id_container_grid = ObjectProperty()
    id_title = ObjectProperty()
    id_signInButton = ObjectProperty()
    id_message = ObjectProperty()
    id_total_activities = ObjectProperty()

    def on_pre_enter(self, *args):
        self.id_title.text = "Plan de Formación"
        self.id_program.values = querys.bringProgramFromEducationPlan()
        self.id_program.bind(text=self.loadLines)
        self.id_line.bind(text=self.loadLevels)
        self.id_level.bind(text=self.loadDescriptions)
        self.id_container_grid.bind(minimum_height=self.id_container_grid.setter('height'))
        self.id_signInButton.bind(on_release=self.checkAll)
        self.id_selectedActivities.bind(on_release=self.selectActivites)
        self.all_activities = []
        self.selected = []

        self.id_program.text = "Programa"
        self.id_line.text = "Linea"
        self.id_level.text = "Nivel"

    def selectActivites(self, *args):
        self.id_message.text = ""
        activities = self.id_container_grid.children
        if len(activities) == 0:
            self.id_message.text = "No hay actividades para seleccionar"
        else:
            for activity in activities:
                activity_data = activity.children[0]
                activity_desc = activity.children[1].text
                activity_desc = activity_desc[8:]
                if activity_data.complete:
                    if not activity_desc in self.selected:
                        self.selected.append(activity_desc)
                        self.all_activities.append({activity_desc: activity_data.text})
        self.id_total_activities.text = f'Actividades Seleccionadas {len(self.all_activities)}'

    def checkAll(self, *args):
        if len(self.all_activities) > 1:
            AcceptFormPlanDeFormacion(self.operator).open()
        else:
            self.id_message.text = "Seleccione más de una actividad"


    def loadLines(self, *args):
        if args[1] != "Programa":
            self.id_line.values = querys.bringLineFromEducationPlan(args[1])

    def loadLevels(self, *args):
        if args[1] != "Linea":
            self.id_level.values = querys.bringLevelFromEducationPlan(self.id_program.text, args[1])

    def loadDescriptions(self, *args):
        if args[1] != "Nivel":
            self.id_container_grid.clear_widgets()
            questions = querys.bringDescriptionsFromEducationPlan(self.id_program.text, self.id_line.text, args[1])
            for idx, quest in enumerate(questions):
                box_layout = BoxLayout(size_hint=(None, None), size=(1040, 40))
                lab = Label(text=f'{idx + 1}]      ' + quest, halign="left", valign="middle", size_hint=(None, None),
                            size=(840, 40), color=(0, 0, 0, 0.85), font_size=24, font_name="montserrat",
                            text_size=(840, 40))
                textInputData = TextInputScrollData()
                box_layout.add_widget(lab)
                box_layout.add_widget(textInputData)
                self.id_container_grid.add_widget(box_layout)

    def on_leave(self, *args):
        dataFormating.plan_de_formacion(self)


class TextInputScrollData(TextInput):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.size = (186, 40)
        self.font_name = "montserrat"
        self.color = (1, 1, 1, 1)
        self.size_hint = (None, None)
        self.halign = "left"
        self.valign = "middle"
        self.background_color = (255 / 255, 255 / 255, 255 / 255, 1)
        self.background_normal = ""
        self.complete = False
        self.class_type = "input"
        self.multiline = False
        self.hint_text = "DD/MM/AAAA"

    def on_text_validate(self, *args):
        if checkings.after_date(self.text):
            self.complete = True
            self.background_color = (7 / 255, 7 / 255, 7 / 255, 0.1)
        else:
            self.complete = False
            self.background_color = (255 / 255, 255 / 255, 255 / 255, 1)


class AcceptFormPlanDeFormacion(class_declaration.PopupFather):
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
