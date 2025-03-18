from gerador_ruas import GeradorRuas as GR


def main():
    # Gerar as ruas para busca e achar a melhor rota
    G = GR()
    G.encontrar_rota()


if __name__ == '__main__':
    main()
