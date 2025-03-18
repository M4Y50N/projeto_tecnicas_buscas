import networkx as nx
import matplotlib.pyplot as plt

class GeradorRuas:

    def __init__(self):
        # Criar um grafo representando um mapa de cidade
        self.G = nx.Graph()

        # Adicionar cruzamentos e distâncias entre eles (arestas)
        nodes = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        self.G.add_nodes_from(nodes)

        # Adicionar ruas (arestas) com pesos representando distâncias
        edges = [
            ("A", "B", 4), ("A", "C", 2), ("B", "C", 5), ("B", "D", 10),
            ("C", "E", 3), ("D", "F", 11), ("E", "D", 4), ("E", "F", 8),
            ("F", "G", 7), ("G", "H", 2), ("H", "I", 6), ("I", "J", 3),
            ("G", "I", 4), ("F", "J", 5), ("E", "H", 9), ("C", "I", 12)
        ]

        for edge in edges:
            self.G.add_edge(edge[0], edge[1], weight=edge[2])

    def encontrar_rota(self):
        # Encontrar a rota mais curta de A até C usando A* (heurística: distância)
        rota = nx.astar_path(self.G, source="A", target="J", weight="weight")
        print(f"Melhor rota: {rota}")

    def desenhar_grafo(self):
        plt.figure(figsize=(6, 4))  # Definir tamanho da figura
        pos = nx.spring_layout(self.G, seed=42)  # Layout do grafo
        nx.draw(self.G, pos, with_labels=True, node_color="lightblue", edge_color="gray", node_size=2000, font_size=12)

        # Adicionar pesos das arestas
        edge_labels = nx.get_edge_attributes(self.G, 'weight')
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=edge_labels, font_size=10)

        plt.title("Mapa das Rotas")
        plt.savefig("grafo.png")  # Salva o gráfico como imagem


