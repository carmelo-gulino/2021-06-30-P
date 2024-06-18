import copy
from time import time

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.localizations = None
        self.graph = None

    def build_graph(self):
        self.localizations = DAO.get_all_localizations()
        self.graph = nx.Graph()
        self.graph.add_nodes_from(self.localizations)
        t1 = time()
        edges = DAO.get_edges()
        for e in edges:
            if e[0] != e[1]:
                self.graph.add_edge(e[0], e[1], weight=e[2])
        t2 = time()
        print(t2-t1)

    def get_graph_details(self):
        return len(self.graph.nodes), len(self.graph.edges)

    def get_statistiche(self, localizzazione):
        statistiche = []
        for n in self.graph.neighbors(localizzazione):
            statistiche.append((n, self.graph[localizzazione][n]["weight"]))
        return statistiche

    def get_cammino(self, localizzazione):
        self.best_sol = []
        self.best_peso = 0
        parziale = [localizzazione]
        self.ricorsione(parziale)
        return self.best_sol, self.best_peso

    def ricorsione(self, parziale):
        peso_sol = self.get_peso(parziale)
        ultimo = parziale[-1]
        if peso_sol > self.best_peso:
            self.best_sol = copy.deepcopy(parziale)
            self.best_peso = peso_sol
        for neighbor in self.graph.neighbors(ultimo):
            if neighbor not in parziale:
                parziale.append(neighbor)
                self.ricorsione(parziale)
                parziale.pop()

    def get_peso(self, parziale):
        peso = 0
        for i in range(len(parziale)-1):
            peso += self.graph[parziale[i]][parziale[i+1]]["weight"]
        return peso
