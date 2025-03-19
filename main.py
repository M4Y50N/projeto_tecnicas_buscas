from gerador_ruas import GeradorRuas as GR


def main():
    origem_rua = "Judite Dantas de Andrade, Mamede Paes Mendonça"
    destino_rua = "Padre Airton Gonçalves lima - sao cristovao"

    # Gerar as ruas para busca e achar a melhor rota
    G = GR()
    G.encontrar_rota(origem_rua, destino_rua)


if __name__ == '__main__':
    main()
