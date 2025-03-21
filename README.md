# Gerador de Rotas com NetworkX e OSMnx

Este projeto gera um grafo representando o mapa de uma cidade e calcula a melhor rota entre dois pontos aleatórios utilizando o algoritmo A*. O grafo é construído a partir dos dados de OpenStreetMap e visualizado com OSMnx e Matplotlib.

## Funcionalidades

- Geração de um grafo real das ruas de uma cidade.
- Cálculo da melhor rota entre dois pontos aleatórios com o algoritmo A*.
- Visualização da rota destacada no mapa completo da cidade.
- Cálculo da distância total entre os pontos da rota.

## Requisitos

- Python 3.8+
- PIP (para instalação das dependências)

### Dependências:

Instale as dependências do projeto utilizando o arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

Se o arquivo `requirements.txt` não existir, você pode instalar as bibliotecas diretamente:

```bash
pip install osmnx networkx matplotlib
```

## Configuração e Execução

1. **Clonar o repositório:**

   ```bash
   git clone https://github.com/usuario/projeto-gerador-rotas.git
   cd projeto-gerador-rotas
   ```

2. **Executar o código:**

   Para rodar o script e gerar o grafo e calcular a rota, utilize:

   ```bash
   python main.py
   ```

3. **Compilação no PyCharm:**

   Se você estiver utilizando o PyCharm e encontrar problemas com a visualização dos gráficos (erro relacionado ao backend gráfico), siga estas instruções:

   - No início do seu script, defina o backend do Matplotlib para evitar conflitos:
   
     ```python
     import matplotlib
     matplotlib.use("TkAgg")  # Evita conflitos com o PyCharm
     ```

   - Se o erro persistir, tente alterar o backend gráfico diretamente nas configurações do PyCharm ou rodar o projeto diretamente via terminal.

## Problemas Comuns

### Problema: Não é possível rodar o código no PyCharm
Solução: Adicione a linha `matplotlib.use("TkAgg")` no topo do seu código para mudar o backend gráfico, permitindo a exibição correta dos gráficos no PyCharm. 

### Problema: O mapa não é carregado (erro com OSMnx)
Solução: Verifique sua conexão com a internet. O OSMnx baixa os dados diretamente do OpenStreetMap, então é necessário estar online.

### Problema: Problemas com dependências no sistema operacional
Solução: Se o seu sistema não suportar algumas dependências, considere rodar o projeto em um ambiente virtual ou utilizando o [Docker](https://www.docker.com/).

### Problema: Erro de "InsufficientResponseError" no OSMnx
Solução: Verifique se o nome da cidade, estado ou país está correto. Certifique-se de que o local digitado existe no banco de dados do OpenStreetMap.

