import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self.page = page
        self.page.title = "Template application using MVC and DAO"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.DARK
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.dd_localizzazione = None
        self.btn_statistiche = None
        self.btn_ricerca = None
        self.txt_result = None

    def load_interface(self):
        # title
        self._title = ft.Text("Hello World", color="blue", size=24)
        self.page.controls.append(self._title)

        self.dd_localizzazione = ft.Dropdown(label="Localizzazione")
        self.btn_statistiche = ft.ElevatedButton(text="Statistiche", on_click=self.controller.handle_statistiche)
        row1 = ft.Row([self.dd_localizzazione, self.btn_statistiche], alignment=ft.MainAxisAlignment.CENTER)
        self.page.controls.append(row1)

        self.btn_ricerca = ft.ElevatedButton(text="Ricerca cammino", on_click=self.controller.handle_cammino)
        row2 = ft.Row([self.btn_ricerca], alignment=ft.MainAxisAlignment.CENTER)
        self.page.controls.append(row2)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self.page.controls.append(self.txt_result)
        self.page.update()
        self.controller.build_graph()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self.page.dialog = dlg
        dlg.open = True
        self.page.update()

    def update_page(self):
        self.page.update()
