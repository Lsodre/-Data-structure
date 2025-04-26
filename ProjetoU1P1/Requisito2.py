import networkx as nx
import matplotlib.pyplot as plt
import os

# Função para carregar e plotar a rede de coautoria de um determinado período
def plot_rede_por_periodo(nome_arquivo, titulo):
    if not os.path.exists(nome_arquivo):
        print(f"Arquivo não encontrado: {nome_arquivo}")
        return

    # Carrega o grafo a partir de um arquivo GEXF
    G = nx.read_gexf(nome_arquivo)

    # Garante que o atributo 'is_permanent' esteja como booleano
    for n, d in G.nodes(data=True):
        d['is_permanent'] = str(d.get('is_permanent', 'False')).lower() == 'true'

    # Calcula o grau de cada nó
    graus = dict(G.degree())
    nx.set_node_attributes(G, graus, 'grau')  # Atribui como atributo do nó

    # Seleciona os 5 nós com maior grau
    top_5 = sorted(graus, key=graus.get, reverse=True)[:5]

    # Gera um layout de posicionamento fixo (para reprodutibilidade)
    pos = nx.spring_layout(G, seed=42)

    # Define o tamanho dos nós com base no grau
    tamanhos = [graus[n]*10 for n in G.nodes()]
    
    # Define a cor dos nós (top 5 em laranja, demais em azul)
    cores_nos = ['orange' if n in top_5 else 'skyblue' for n in G.nodes()]

    # Inicializa listas para estilos das arestas
    larguras = []
    cores_arestas = []

    # Define a largura e cor das arestas com base nas citações e se são entre permanentes
    for u, v, data in G.edges(data=True):
        try:
            citation = float(data.get('citation_num', 1))  # Número de citações
        except:
            citation = 1.0
        larguras.append(citation / 20)  # Escala da largura da aresta

        u_perm = G.nodes[u].get('is_permanent', False)
        v_perm = G.nodes[v].get('is_permanent', False)

        # Arestas entre permanentes são vermelhas, outras pretas
        if u_perm and v_perm:
            cores_arestas.append('red')
        else:
            cores_arestas.append('black')

    # Inicia a figura para plotagem
    plt.figure(figsize=(14, 10))

    # Desenha as arestas com as configurações definidas
    nx.draw_networkx_edges(G, pos, alpha=0.5, edge_color=cores_arestas, width=larguras)

    # Desenha os nós com tamanho e cor apropriados
    nx.draw_networkx_nodes(G, pos, node_color=cores_nos, node_size=tamanhos, alpha=0.9)

    # Adiciona rótulo apenas aos 5 nós com maior grau
    labels = {n: n for n in top_5}
    nx.draw_networkx_labels(G, pos, labels=labels, font_size=12, font_color='green',font_weight='bold')

    # Configurações do gráfico
    plt.title(titulo, fontsize=16)
    plt.axis('off')  # Remove os eixos
    plt.tight_layout()  # Ajusta layout
    plt.show()  # Exibe o gráfico

# Executa a função para cada arquivo de rede correspondente a um período
plot_rede_por_periodo("2010-2012.gexf", "Rede de Coautoria PPgEEC - 2010 a 2012")
plot_rede_por_periodo("2013-2016.gexf", "Rede de Coautoria PPgEEC - 2013 a 2016")
plot_rede_por_periodo("2017-2020.gexf", "Rede de Coautoria PPgEEC - 2017 a 2020")
plot_rede_por_periodo("2021-2024.gexf", "Rede de Coautoria PPgEEC - 2021 a 2024")
