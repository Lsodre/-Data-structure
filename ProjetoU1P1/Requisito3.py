import networkx as nx
import os
import matplotlib.pyplot as plt
import numpy as np

# === Construção da rede geral de coautorias de 2010 a 2024 ===
G_geral = nx.Graph()
for ano in range(2010, 2025):
    arquivo = f"{ano}_authors_network.gexf"
    if os.path.exists(arquivo):
        G_ano = nx.read_gexf(arquivo)  # Carrega o grafo do ano
        G_geral.add_nodes_from(G_ano.nodes(data=True))  # Adiciona nós com atributos
        G_geral.add_edges_from(G_ano.edges(data=True))  # Adiciona arestas com atributos

# === Cálculo dos graus dos nós ===
graus = dict(G_geral.degree())  # Dicionário de grau por nó
valores_grau = list(graus.values())  # Lista dos graus

# === Definição do limiar X (grau >= média +  desvio padrão) ===
media = np.mean(valores_grau)
desvio = np.std(valores_grau)
X = int(media + desvio)  # Limiar para selecionar nós mais conectados

print(f"X escolhido (média + desvio): {X}")

# === Criação de subgrafo com os nós cujo grau >= X ===
nodos_filtrados = [n for n, g in graus.items() if g >= X]
subgrafo = G_geral.subgraph(nodos_filtrados)  # Subgrafo dos mais conectados

# === Cálculo das densidades das redes ===
densidade_geral = nx.density(G_geral)
densidade_sub = nx.density(subgrafo)

print(f"Densidade geral: {densidade_geral:.4f}")
print(f"Densidade do subgrafo: {densidade_sub:.4f}")

# === Construção da rede ego (nó mais conectado e seus vizinhos) ===
n_top = max(graus, key=graus.get)  # Nó com maior grau
ego = nx.ego_graph(G_geral, n_top)  # Rede ego centrada nesse nó

# === Visualização: três gráficos lado a lado ===
fig, axs = plt.subplots(1, 3, figsize=(24, 8))

# Função auxiliar para desenhar grafos
def desenhar_grafo(G, titulo, ax, destaque=None):
    pos = nx.spring_layout(G, seed=42, k=0.3)  # Layout com semente fixa
    graus = dict(G.degree())
    max_grau = max(graus.values()) if graus else 1
    tamanhos = [100 + 800 * (graus[n] / max_grau) for n in G.nodes()]  # Escala proporcional ao grau

    # Desenha os nós e arestas
    nx.draw_networkx_nodes(G, pos, node_size=tamanhos, node_color='skyblue', alpha=0.8, ax=ax)
    nx.draw_networkx_edges(G, pos, alpha=0.3, ax=ax)

    # Destaque de um nó específico (caso de rede ego)
    if destaque and destaque in G:
        nx.draw_networkx_nodes(G, pos, nodelist=[destaque], node_color='red',
                               node_size=1200, label="Ego", ax=ax)
        nx.draw_networkx_labels(G, pos, labels={destaque: destaque}, font_size=12, font_weight='bold', ax=ax)

    ax.set_title(titulo, fontsize=14)
    ax.axis('off')  # Remove os eixos

# === Execução dos gráficos ===
desenhar_grafo(G_geral, "Rede Geral de Coautoria (2010–2025)", axs[0])
desenhar_grafo(subgrafo, f"Subgrafo (grau {X})", axs[1])
desenhar_grafo(ego, f"Rede Ego de {n_top}", axs[2], destaque=n_top)

# Ajuste final do layout e exibição
plt.tight_layout()
plt.show()
