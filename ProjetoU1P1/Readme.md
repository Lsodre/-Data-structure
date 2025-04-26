Projeto Unidade 1: 
Análises de rede de co-autoria extraídos PPgEEC.

Aluno: Leonardo Sodré

    O objetivo desse trabalho é analisar a rede de coautoria do PPgEEC no período de 2010 a 2025 seguindo a seguintes métricas :

-> Densidade da rede : representa o quanto a rede é povoada ou conectada.

-> Número de vértices : representa o número de pesquisadores(tamanho da rede)

-> Número de arestas :representa o número de colaboração(conexão) direta entre pesquisadores

-> Número médio de vizinhos : é a média de colaboração que cada pesquisador tem

-> Distribuição do número de vizinhos: descreve como ocorre a distribuição de arestas(vizinhos) entre os pesquisadores(vértice).


    A seguir obtive os seguintes resultados:

![Texto Alternativo](https://github.com/Lsodre/-Data-structure/blob/main/ProjetoU1P1/Figure_1.png)

    Figura 1: podemos ver que o número de arestas cai em períodos de avaliação, com exceção de 2024 que obteve próximo ao máximo.
     O número de vértices é estável em torno de 500, a densidade variou entre 0,02 e 0,01 aproximadamente e grau médio variou próximo de 8 a 14.

![Texto Alternativo](https://github.com/Lsodre/-Data-structure/blob/main/ProjetoU1P1/Figure_2.png)

    Figura 2: podemos ver o comportamento da distribuição do número de vizinhos.

    A seguir os grafos para analisar o comportamento das redes nos períodos de avaliação do PPgEEC (2010-2012, 2013-2016, 2017-2020, 2021-2024), Onde o tamanho do vértice é proporcional ao número de vizinhos, em destaque os cinco vértices com mais vizinhos, as arestas vermelhas indicam citações entre membros permanentes do programa, caso contrário a aresta é preta,e a largura da aresta é proporcional à quantidade de citações 

![Texto Alternativo](https://github.com/Lsodre/-Data-structure/blob/main/ProjetoU1P1/Figure_3.png)

    Figura 3: Podemos ver que nesse período os quatros pesquisadores mais citados fazem a densidade da rede tender para esse lado, e também eles  estão conectados diretamente entre si.

![Texto Alternativo](https://github.com/Lsodre/-Data-structure/blob/main/ProjetoU1P1/Figure_4.png)

    Figura 4: Nesse período podemos ver a rede um pouco mais balanceada, com os 5 mais citados próximos,e a rede povoada em torno deles, isso pode indicar que pode haver uma dependência desses pesquisadores nessa rede.
  
![Texto Alternativo](https://github.com/Lsodre/-Data-structure/blob/main/ProjetoU1P1/Figure_5.png)

    Figura 5: podemos ver que  a rede se distribuiu melhor em torno dos pesquisadores mais citados nesse período, indicando uma dependência maior.
  
![Texto Alternativo](https://github.com/Lsodre/-Data-structure/blob/main/ProjetoU1P1/Figure_6.png)

    Figura 6: A distribuição deu uma leve desbalanceada em comparação com o período anterior, isso pode indicar que a dependência caiu, e nesse período a rede diminuiu, indicando que citações entre colegas da rede caiu.

    E por fim vamos analisar a rede em todo período

![Texto Alternativo](https://github.com/Lsodre/-Data-structure/blob/main/ProjetoU1P1/Figure_7.png)

    Figura 7: Podemos ver que a rede geral é bem distribuída em todo período, o subgrafo com grau 59 foi escolhido a partir da média mais o desvio padrão da rede geral, essa métrica foi escolhida pois destaca quantos são os nós mais significativos e a distribuição na rede, podemos dizer que há 59 pesquisadores mais influentes no programa e comparando com o grafo geral a distribuição se mantém parecida, na terceira rede podemos ver que esse pesquisador é muito citado no programa, quase mantendo a mesma distribuição da rede geral.

    Esse projeto teve auxilio do Chatgpt apenas para gerar os gráficos 
