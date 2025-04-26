import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns
import os
import numpy as np
import pandas as pd
from scipy.interpolate import make_interp_spline

# Configurações visuais dos gráficos
sns.set(style="whitegrid")
plt.rcParams.update({"figure.figsize": (12, 6)})

# Lista de anos a analisar
anos = list(range(2010, 2026))

# Inicializa listas para armazenar métricas
densidades, num_vertices, num_arestas, graus_medios = [], [], [], []
distribuicoes = {}
anos_validos = []

# === Coleta das métricas dos grafos ===
for ano in anos:
    arquivo = f"{ano}_authors_network.gexf"
    if os.path.exists(arquivo):  # Verifica se o arquivo existe
        G = nx.read_gexf(arquivo)  # Lê o grafo do arquivo GEXF
        anos_validos.append(ano)
        densidades.append(nx.density(G))  # Calcula densidade do grafo
        num_vertices.append(G.number_of_nodes())  # Número de nós
        num_arestas.append(G.number_of_edges())  # Número de arestas
        graus = [grau for _, grau in G.degree()]  # Lista dos graus dos nós
        graus_medios.append(np.mean(graus) if graus else 0)  # Grau médio
        distribuicoes[ano] = graus  # Salva a distribuição dos graus

# === Parte 1: Curvas das métricas ===

plt.figure()
labels = ['Densidade', 'Nº de vértices', 'Nº de arestas', 'Grau médio']
cores = sns.color_palette("tab10")
dados = [densidades, num_vertices, num_arestas, graus_medios]

# Gera as curvas sem suavização
for i, y in enumerate(dados):
    plt.plot(anos_validos, y, label=labels[i], color=cores[i], linewidth=2)
    plt.scatter(anos_validos[-1], y[-1], s=50, color=cores[i], edgecolors='black', zorder=5)

# Linhas verticais marcando os anos de avaliação
for marco in [2012, 2016, 2020, 2024]:
    plt.axvline(marco, color="gray", linestyle="--", linewidth=1)


# Configurações finais do gráfico
plt.title("Evolução das Métricas da Rede de Coautorias (2010–2025)", fontsize=14)
plt.xlabel("Ano")
plt.ylabel("Valor das métricas")
plt.legend()
plt.tight_layout()
plt.show()

# === Parte 2: Ridgeline Plot (Distribuição do Grau) ===

dados = []
arestas_por_ano = {}

# Lê novamente os grafos para compilar a distribuição dos graus
for ano in range(2010, 2026):
    nome_arquivo = f"{ano}_authors_network.gexf"
    if os.path.exists(nome_arquivo):
        G = nx.read_gexf(nome_arquivo)
        graus = [grau for _, grau in G.degree()]
        arestas_por_ano[ano] = G.number_of_edges()
        for g in graus:
            dados.append({'Ano': ano, 'Grau': g})

# Cria DataFrame com os dados de grau por ano
df = pd.DataFrame(dados)

# Mapeia cores com base no número de arestas por ano
anos_unicos = sorted(df['Ano'].unique())
valores = np.array([arestas_por_ano[ano] for ano in anos_unicos])
norm = plt.Normalize(valores.min(), valores.max())  # Normalização para mapa de cor
paleta = sns.color_palette("rocket", as_cmap=True)
cores_map = {ano: paleta(norm(arestas_por_ano[ano])) for ano in anos_unicos}
df['Cor'] = df['Ano'].map(cores_map)  # Aplica cor correspondente ao DataFrame

# Configura estilo para o gráfico ridgeline
sns.set(style="white", rc={"axes.facecolor": (0, 0, 0, 0)})

# Cria o grid do gráfico, uma linha por ano
g = sns.FacetGrid(df, row="Ano", hue="Ano", aspect=10, height=0.5,
                  palette=[cores_map[ano] for ano in anos_unicos], xlim=(0, 25))

# Plota KDE preenchido
g.map(sns.kdeplot, "Grau",
      bw_adjust=0.5, fill=True, clip=(0, 25), linewidth=1.5, alpha=1)

# Plota linha branca de contorno
g.map(sns.kdeplot, "Grau",
      bw_adjust=0.5, clip=(0, 25), color="w", lw=1)

# Função auxiliar para rotular os anos nas curvas
def label(x, color, label):
    ax = plt.gca()
    ax.text(0, 0.1, label, fontweight="bold", color=color,
            ha="left", va="center", fontsize=8)

# Aplica rótulo a cada linha
g.map(label, "Grau")

# Ajustes finais do layout do gráfico
g.figure.subplots_adjust(hspace=-0.75)
g.set_titles("")
g.set(yticks=[], xlabel="Número de Vizinhos (Grau)", ylabel=None)
g.despine(bottom=True, left=True)

# Título geral do gráfico
plt.suptitle("Distribuição do Número de Vizinhos por Ano (2010–2025)\n", fontsize=14)
plt.tight_layout()
plt.show()