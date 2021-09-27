# coding=utf-8
from kivy.app import App
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager
from windows import Login, Panel, InformacionGeneral, DiagnosticoPerfilProductivo, IdeaDeNegocio, UnidadDeNegocio, \
    CaracterizacionAmpliada, Monitoreo, DiagnosticoEmpresarial, PlanDeFormacion, ActividadDeFormacion, \
    PlanDeImplementacion, ActividadDeImplementacion


class MyApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sm = ScreenManager()

    def build(self):
        LabelBase.register(name='montserrat', fn_regular='fonts/Montserrat-Regular.ttf',
                           fn_bold='fonts/Montserrat-SemiBold.ttf')

        Builder.load_file(f"windows/Login.kv")
        Builder.load_file(f"windows/Panel.kv")
        Builder.load_file(f"windows/InformacionGeneral.kv")
        Builder.load_file(f"windows/DiagnosticoPerfilProductivo.kv")
        Builder.load_file(f"windows/IdeaDeNegocio.kv")
        Builder.load_file(f"windows/UnidadDeNegocio.kv")
        Builder.load_file(f"windows/CaracterizacionAmpliada.kv")
        Builder.load_file(f"windows/Monitoreo.kv")
        Builder.load_file(f"windows/DiagnosticoEmpresarial.kv")
        Builder.load_file(f"windows/PlanDeFormacion.kv")
        Builder.load_file(f"windows/ActividadDeFormacion.kv")
        Builder.load_file(f"windows/PlanDeImplementacion.kv")
        Builder.load_file(f"windows/ActividadDeImplementacion.kv")

        Builder.load_file('declarations/templates_declaration.kv')

        self.sm.add_widget(Login.LoginScreen(name='Login'))
        self.sm.add_widget(Panel.PanelScreen(name="Panel"))
        self.sm.add_widget(InformacionGeneral.InformacionGeneralScreen(name="InformacionGeneral"))
        self.sm.add_widget(
            DiagnosticoPerfilProductivo.DiagnosticoPerfilProductivoScreen(name="DiagnosticoPerfilProductivo"))
        self.sm.add_widget(IdeaDeNegocio.IdeaDeNegocioScreen(name="IdeaDeNegocio"))
        self.sm.add_widget(UnidadDeNegocio.UnidadDeNegocioScreen(name="UnidadDeNegocio"))
        self.sm.add_widget(CaracterizacionAmpliada.CaracterizacionAmpliadaScreen(name="CaracterizacionAmpliada"))
        self.sm.add_widget(Monitoreo.MonitoreoScreen(name="Monitoreo"))
        self.sm.add_widget(DiagnosticoEmpresarial.DiagnosticoEmpresarialScreen(name="DiagnosticoEmpresarial"))
        self.sm.add_widget(PlanDeFormacion.PlanDeFormacionScreen(name="PlanDeFormacion"))
        self.sm.add_widget(ActividadDeFormacion.ActividadDeFormacionScreen(name="ActividadDeFormacion"))
        self.sm.add_widget(PlanDeImplementacion.PlanDeImplementacionScreen(name="PlanDeImplementacion"))
        self.sm.add_widget(ActividadDeImplementacion.ActividadDeImplementacionScreen(name="ActividadDeImplementacion"))
        self.sm.current = 'Login'

        Factory.LoginProjectPopup.changeWindow = self.changeToPanel
        Factory.EmergentNuevoBeneficiario.changeWindow = self.changeToInformacionGeneral
        Factory.AcceptForm.changeWindow = self.changeToDiagnosticoPerfilProductivo
        Factory.AcceptFormDiagno.changeWindowEntrep = self.changeToIdeaDeNegocio
        Factory.AcceptFormDiagno.changeWindowBussin = self.changeToUnidadDeNegocio
        Factory.AcceptFormIdea.changeWindow = self.changeToPanel
        Factory.AcceptFormUnit.changeWindow = self.changeToPanel

        Factory.CaracterizacionAmpliadaButton.changeWindow = self.changeToCaracterizacionAmpliada
        Factory.MonitoreoButton.changeWindow = self.changeToMonitoreo
        Factory.PlanDeImplementacionButton.changeWindow = self.changeToActividadDeImplementacion
        Factory.PlanDeImplementacionButton.changeToPlan = self.changeToPlanDeImplementacion
        Factory.PlanDeFormacionButton.changeWindow = self.changeToActividadDeFormacion
        Factory.PlanDeSeguimientoButton.changeWindow = self.changeToPlanDeImplementacion

        Factory.AcceptFormCaracterizacionAmpliada.changeWindow = self.changeToMonitoreo
        Factory.AcceptFormMonitoreo.changeWindow = self.changeToDiagnosticoEmpresarial
        Factory.AcceptFormDiagnosticoEmpresarial.changeWindow = self.changeToPanel
        Factory.AcceptFormPlanDeFormacion.changeWindow = self.changeToPanel
        Factory.AcceptFormActividadDeFormacion.changeWindow = self.changeToPanel
        Factory.AcceptFormPlanDeImplementacion.changeWindow = self.changeToPanel
        Factory.AcceptFormActividadDeImplementacion.changeWindow = self.changeToPanel
        Factory.AcceptFormCaracterizacionAmpliada.changeToUnidad = self.changeToUnidadDeNegocio
        Factory.AcceptFormUnit.changeToMonitoreo = self.changeToMonitoreo
        Factory.PlanDeFormacionButton.changeToPlan = self.changeToPlanDeFormacion
        Factory.SeleccionarActividad.changeWindow = self.changeToPanel

        return self.sm

    def changeToLogin(self, *args):
        self.sm.current = 'Login'

    def changeToPanel(self, *args):
        self.sm.current = 'Panel'

    def changeToInformacionGeneral(self, *args):
        self.sm.current = 'InformacionGeneral'

    def changeToDiagnosticoPerfilProductivo(self, *args):
        self.sm.current = 'DiagnosticoPerfilProductivo'

    def changeToIdeaDeNegocio(self, *args):
        self.sm.current = 'IdeaDeNegocio'

    def changeToUnidadDeNegocio(self, *args):
        self.sm.current = 'UnidadDeNegocio'

    def changeToCaracterizacionAmpliada(self, *args):
        self.sm.current = 'CaracterizacionAmpliada'

    def changeToMonitoreo(self, *args):
        self.sm.current = 'Monitoreo'

    def changeToDiagnosticoEmpresarial(self, *args):
        self.sm.current = 'DiagnosticoEmpresarial'

    def changeToPlanDeFormacion(self, *args):
        self.sm.current = 'PlanDeFormacion'

    def changeToActividadDeFormacion(self, *args):
        self.sm.current = 'ActividadDeFormacion'

    def changeToPlanDeImplementacion(self, *args):
        self.sm.current = 'PlanDeImplementacion'

    def changeToActividadDeImplementacion(self, *args):
        self.sm.current = 'ActividadDeImplementacion'


if __name__ == '__main__':
    Window.size = (1280, 800)
    Window.left = 45
    Window.top = -25
    Window.clearcolor = [1, 1, 1, 1]
    Window.softinput_mode = "below_target"
    corporation = MyApp()
    corporation.run()
