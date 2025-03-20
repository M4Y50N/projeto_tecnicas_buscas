import random

import osmnx as ox
import networkx as nx
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("TkAgg")  # Se for usar no Pycharm descomente essa linha


class GeradorRuas:

    def __init__(self, pais="brasil", cidade="itabaiana", estado="sergipe"):
        # Criar um grafo representando um mapa de cidade
        self.G = None
        self.pais = pais
        self.cidade = cidade
        self.estado = estado
        self.__transformar_ruas_em_grafos(self.pais, self.cidade, self.estado)

    def encontrar_rota(self, origem_rua=None, destino_rua=None):
        try:
            # Geocodificar os endereços para obter coordenadas geográficas
            # Se a origem ou o destino não for informado o programa irá gerar um aleatório
            origem_coord = ox.geocode(f"{origem_rua}, {self.cidade}, {self.estado}, {self.pais}") if origem_rua \
                else random.choice(list(self.G.nodes))
            destino_coord = ox.geocode(f"{destino_rua}, {self.cidade}, {self.estado}, {self.pais}") if destino_rua \
                else random.choice(list(self.G.nodes))

        except BaseException as error:
            raise error
        else:
            # Encontrar os nós mais próximos dessas coordenadas no grafo
            origem = ox.nearest_nodes(self.G, origem_coord[1], origem_coord[0]) if origem_rua \
                else origem_coord
            destino = ox.nearest_nodes(self.G, destino_coord[1], destino_coord[0]) if destino_rua \
                else destino_coord

            # Encontrar a melhor rota usando A* com heurística de distância
            rota = nx.astar_path(self.G, origem, destino, weight="length")

            # Calcular a distância total da rota
            distancia = sum(self.G[u][v][0]['length'] for u, v in zip(rota[:-1], rota[1:]))
            distancia_km = round(distancia / 1000, 2)  # Converter para quilômetros

            # Plotar a rota no mapa
            fig, ax = plt.subplots(figsize=(10, 8))
            ax.set_title(f"Melhor Rota Encontrada pelo A*. {distancia_km}km")

            ### Não alterar a ordem de plot
            # Primeiro ele vai plotar a melhor rota encontrada
            ox.plot_graph_route(self.G, rota, ax=ax, route_linewidth=4, node_size=50, route_color="blue",
                                show=False, close=False)

            # Depois ele vai plotar o mapa da cidade "por cima da melhor rota encontrada"
            ox.plot_graph(self.G, ax=ax, node_color="gray", edge_color="lightgray", node_size=10, bgcolor="white")
            ####

            print(f"Origem: {origem_rua}, Destino: {destino_rua}, Distância: {distancia_km}km")

    def __transformar_ruas_em_grafos(self, pais="brasil", cidade="itabaiana", estado="sergipe"):
        try:
            localidade = f"{cidade}, {estado}, {pais}"

            # Baixar o grafo real das ruas da cidade
            self.G = ox.graph_from_place(localidade, network_type="drive")  # "drive" obtém apenas ruas para veículos
        except ox._errors.InsufficientResponseError as error:
            raise error
