import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self.chosen_business = None
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def build_graph(self):
        self.model.build_graph()
        for localizzazione in self.model.localizations:
            self.view.dd_localizzazione.options.append(ft.dropdown.Option(localizzazione))
        self.view.txt_result.controls.clear()
        n_nodi, n_archi = self.model.get_graph_details()
        self.view.txt_result.controls.append(ft.Text(f"Il grafo creato ha {n_nodi} nodi e {n_archi} archi"))
        self.view.update_page()

    def handle_statistiche(self, e):
        self.chosen_localizzazione = self.view.dd_localizzazione.value
        neighbors = self.model.get_statistiche(self.chosen_localizzazione)
        self.view.txt_result.controls.clear()
        self.view.txt_result.controls.append(ft.Text(f"Adiacenti a {self.chosen_localizzazione}:"))
        for neighbor in neighbors:
            self.view.txt_result.controls.append(ft.Text(f"{neighbor[0]}: {neighbor[1]}"))
        self.view.update_page()

    def handle_cammino(self, e):
        path, peso = self.model.get_cammino(self.chosen_localizzazione)
        self.view.txt_result.controls.clear()
        self.view.txt_result.controls.append(ft.Text(f"Il cammino più lungo da {self.chosen_localizzazione} "
                                                     f"ha peso {peso} ed è il seguente"))
        for p in path:
            self.view.txt_result.controls.append(ft.Text(f"{p}"))
        self.view.update_page()


    @property
    def view(self):
        return self._view

    @property
    def model(self):
        return self._model

