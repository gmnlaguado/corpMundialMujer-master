
# coding=utf-8
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from declarations import querys, dataFormating, class_declaration
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox


class DiagnosticoPerfilProductivoScreen(Screen):
    payeeDocument = None
    payeeType = None

    id_container_grid: ObjectProperty()
    id_message: ObjectProperty()
    id_signInButton: ObjectProperty()

    def on_pre_enter(self):
        if not len(self.id_container_grid.children) > 0:
            self.id_signInButton.bind(on_release=self.checkAll)
            questions = querys.parametricList('preguntas_de_diagnostico')
            self.id_container_grid.bind(minimum_height=self.id_container_grid.setter('height'))
            for idx, quest in enumerate(questions):
                lab = Label(text=f'{idx + 1}]  ' + quest, halign="justify", valign="middle", size_hint=(None, None),
                            size=(815, 51), color=(0, 0, 0, 0.85), font_size=20, font_name="montserrat",
                            text_size=(815, 51))
                box_container = BoxLayout()
                for i in ['Si', 'MasMenos', 'No']:
                    check = CheckBox(group=f"pregunta_{idx + 1}", color=(0, 1, 0, 1))
                    box_container.add_widget(check)
                self.id_container_grid.add_widget(lab)
                self.id_container_grid.add_widget(box_container)

        for idx1, grid in enumerate(self.id_container_grid.children):
            if len(grid.children) > 0:
                for idx2, box in enumerate(grid.children):
                    if box.active:
                        self.id_container_grid.children[idx1].children[idx2].active = False

    def checkAll(self, *args):
        self.id_message.text = ""
        for grid in self.id_container_grid.children:
            if len(grid.children) > 0 and not True in [box.active for box in grid.children]:
                self.id_message.text = "Faltan preguntas por responder"

        if self.id_message.text == "":
            diagnostic_answers = []
            for grid in self.id_container_grid.children:
                if len(grid.children) > 0:
                    repp = [box.active for box in grid.children][::-1].index(True)
                    diagnostic_answers.append(repp)

            diagnostic_answers = diagnostic_answers[::-1]
            diagnostic_answers.insert(0, self.payeeDocument)
            dataFormating.productionProfileDiagData(diagnostic_answers)
            AcceptFormDiagno(self.payeeType).open()


class AcceptFormDiagno(class_declaration.PopupFather):
    id_acceptButton = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.payeeType = args[0]
        self.id_acceptButton.bind(on_release=self.on_validate)

    def on_pre_open(self):
        self.title = f"ODP Operario verifique que la información es correcta antes de continuar"
        
    def on_validate(self, *args):
        self.dismiss()
        if self.payeeType == "Emprendedor":
            self.changeWindowEntrep()
        else:
            self.changeWindowBussin()

    def changeWindowEntrep(self, *args):
        pass

    def changeWindowBussin(self, *args):
        pass