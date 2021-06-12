import pandas as pd
import plotly.express as px

# Passo 1: Ler a base de dados.
# Passo 2: Visualizar e tratar a base de dados.
# Passo 3: Analisar a base de dados.
# Passo 4: Construir uma analise para tentar prever a quantidade de vendas em um novo país.

# Passo 1:
vendas_por_pais_df = pd.read_csv("sales_per_country.csv", error_bad_lines=False, encoding="ISO-8859-1")

# Passo 2: 
# Foi feito manualmente na base de dados, pois ela estava impossível de analisar.

# Passo 3:
display(vendas_por_pais_df)
display(vendas_por_pais_df.describe())

# Observações superficiais:
# 1 - Parece que, interessantemente, a população não tem grande influência nas vendas
# a variável que mais aparenta impactar as vendas é o GNP per Capita.

# Passo 4:
for coluna in vendas_por_pais_df:
    grafico = px.bar(vendas_por_pais_df, y="Peptamant Plus Sales (M$)", x=coluna)
    grafico.show()

# Premissas:
    # 1. Os países com mais compradores são aqueles com a % do PIB 
    #    para investimento em saúde de 4,4 à 5,7% com o auge sendo em 4,8%.
    # 2. Países com a taxa dedesemprego de 6, 9.1 e 10% são os maiores compradores
    #    sendo 8% a média, com um desvio padrão de 3.
    # 3. O PIB per Capita dos maiores compradores é de 43.54k à 44.51k
    # 4. Países com a população entre 61-62 milhões estão com os maiores compradores.
    # 5. 75% dos compradores tem o PIB per capita de 50k pra baixo, tendo 36k de média.
# Conclusões:
    # 1. Países com PIB per Capita abaixo de 10k, 
    #    não costumam ser boas escolhas.
    # 2. Países com desemprego inferior à 10% tendem a ser boas escolhas.
