import random

import osmnx as ox
import networkx as nx
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("TkAgg")  # Define o backend para evitar conflitos com o PyCharm


class GeradorRuas:

    def __init__(self, pais="brasil", cidade="itabaiana", estado="sergipe"):
        # Criar um grafo representando um mapa de cidade
        self.G = None
        self.__transformar_ruas_em_grafos(pais, cidade, estado)

    def encontrar_rota(self):
        # Escolher dois pontos aleatórios como origem e destino
        origem = random.choice(list(self.G.nodes))
        destino = random.choice(list(self.G.nodes))

        # Encontrar a melhor rota usando A* com heurística de distância
        rota = nx.astar_path(self.G, origem, destino, weight="length")

        # Plotar a rota no mapa
        fig, ax = plt.subplots(figsize=(10, 8))
        ox.plot_graph_route(self.G, rota, ax=ax, route_linewidth=4, node_size=50, route_color="blue", node_color="red")
        ax.title("Melhor Rota Encontrada pelo A*")

        print(f"Origem: {origem}, Destino: {destino}")

    def __transformar_ruas_em_grafos(self, pais="brasil", cidade="itabaiana", estado="sergipe"):
        try:
            localidade = f"{cidade}, {estado}, {pais}"

            # Baixar o grafo real das ruas da cidade
            self.G = ox.graph_from_place(localidade, network_type="drive")  # "drive" obtém apenas ruas para veículos
        except ox._errors.InsufficientResponseError as error:
            print(error)
        else:
            # Mostrar o grafo real do mapa
            fig, ax = plt.subplots(figsize=(10, 8))
            ox.plot_graph(self.G, ax=ax, node_color="red", edge_color="gray", node_size=10, bgcolor="white")
            ax.set_title(f"Mapa Real das Ruas de {cidade}")
            plt.savefig("localidade.png")

