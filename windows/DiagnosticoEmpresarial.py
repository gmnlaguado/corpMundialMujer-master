# coding=utf-8
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from declarations import querys, class_declaration, dataFormating
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
import statistics
from windows import Monitoreo


class DiagnosticoEmpresarialScreen(Screen):
    project = None
    operator = None
    payeeDocument = None
    home = False

    id_container_grid_1 = ObjectProperty()
    id_message = ObjectProperty()
    id_signInButton = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)

        self.puntajes = [10, 7, 4, 0]

        questions = querys.parametricList('preguntas_diagnostico_empresarial')
        categories = querys.parametricList('categorias_diagnostico_empresarial')
        answers = querys.parametricList('respuestas_diagnostico_empresarial')
        counter = 0
        totalAnswers = 0
        self.id_container_grid_1.bind(minimum_height=self.id_container_grid_1.setter('height'))
        for idx, quest in enumerate(questions):
            # Question Category
            if idx % 5 == 0 and counter < len(categories):
                cat = Label(text=categories[counter], halign="center", valign="middle", size_hint=(None, None),
                            size=(853, 51), color=(0, 0, 0, 0.85), font_size=30, font_name="montserrat",
                            text_size=(853, 51))

                counter += 1
                self.id_container_grid_1.add_widget(cat)

            # Questions Statement
            box_container = BoxLayout(size_hint=(None, None), size=(1035, 110))
            lab = Label(text=quest, halign="center", valign="middle", size_hint=(None, None),
                        size=(294, 109), color=(0, 0, 0, 0.85), font_size=18, font_name="montserrat",
                        text_size=(294, 109))
            box_container.add_widget(lab)

            # Options to Answer with its checboxes
            answers_container = BoxLayout(size_hint=(None, None), size=(696, 110), spacing=12, orientation="vertical")
            for i in range(4):
                # Single Option
                line_container = BoxLayout(size_hint=(None, None), size=(696, 20))
                ans = Label(text=answers[totalAnswers], halign="center", valign="middle", size_hint=(None, None),
                            size=(661, 18), color=(0, 0, 0, 0.85), font_size=12, font_name="montserrat",
                            text_size=(661, 18))
                check = CheckBox(group=f"pregunta_{counter}_opcion{idx}", color=(0, 1, 0, 1))
                totalAnswers += 1
                line_container.add_widget(ans)
                line_container.add_widget(check)
                answers_container.add_widget(line_container)
            box_container.add_widget(answers_container)

            self.id_container_grid_1.add_widget(box_container)

        self.id_signInButton.bind(on_release=self.checkAll)

    def checkAll(self, *args):
        total_answers = []
        self.id_message.text = ""
        for grid in self.id_container_grid_1.children:
            if len(grid.children) > 0:
                for grid_children in grid.children:
                    if len(grid_children.children) > 0:
                        grupo = []
                        for grid_grandson in grid_children.children:
                            grupo.append(grid_grandson.children[0].active)
                            if len(grupo) == 4:
                                total_answers.append(grupo)
                                grupo = []
        for answ in total_answers:
            if not True in answ:
                self.id_message.text = "Faltan preguntas por responder"
        if self.id_message.text == "":
            self.total_answers = total_answers[::-1]

            puntaje_pregunta = []
            puntaje_categoria = []
            conteo_categoria = 0
            puntaje_total = 0
            porcentaje_categoria = [0.12, 0.12, 0.1, 0.15, 0.15, 0.12, 0.07, 0.05, 0.12]
            for answer in self.total_answers:
                puntaje = self.puntajes[answer.index(True)]
                puntaje_pregunta.append(puntaje)
                if len(puntaje_pregunta) == 5:
                    resultado_puntaje = statistics.mean(puntaje_pregunta)
                    puntaje_categoria.append(resultado_puntaje)
                    resultado_puntaje = resultado_puntaje * porcentaje_categoria[conteo_categoria]
                    conteo_categoria += 1
                    puntaje_pregunta = []
                    puntaje_total += resultado_puntaje
            self.puntaje_total = puntaje_total
            self.puntaje_categoria = puntaje_categoria
            class_declaration.MessagePopup(f'Puntaje {puntaje_total:.3f}').open()
            AcceptFormDiagnosticoEmpresarial(self.operator).open()

    def on_leave(self, *args):
        dataFormating.diagnostico_empresarial(self, Monitoreo.MonitoreoScreen.numero_de_monitoreo)


class AcceptFormDiagnosticoEmpresarial(class_declaration.PopupFather):
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