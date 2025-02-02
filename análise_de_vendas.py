# -*- coding: utf-8 -*-
"""Análise de Vendas.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QzeAc0-0L0okIF3gWJDrF6zTJp8US5B2
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import date

data = pd.read_csv('Online Sales Data.csv')

data.head()

data.info()

# Convertendo Date em DateTime
data['Date'] = pd.to_datetime(data['Date'])

# Criando coluna mes e ano
data['mes_ano']= data['Date'].dt.to_period('M')

data.info()

data.duplicated().sum()

data.isnull().sum()

data.describe()

# identificar a categoria mais vendida para cada região.
venda_categoria_regiao = data.groupby(['Region','Product Category'])['Units Sold'].sum().sort_values(ascending=False)
venda_categoria_regiao

# Selecionar a categoria mais vendida em cada região
venda_categoria_regiao_max = venda_categoria_regiao.groupby('Region').head(1)

print(venda_categoria_regiao_max)

# Resetando o índice para transformar o MultiIndex em colunas
venda_categoria_regiao_max_reset = venda_categoria_regiao_max.reset_index()
venda_categoria_regiao_max_reset

# Criando o gráfico de barras com a categoria mais vendida por região
sns.barplot(x='Region', y='Units Sold', hue='Product Category', data=venda_categoria_regiao_max_reset)
# Inclinando os rótulos do eixo X para melhor leitura
plt.title('Categoria Mais Vendida por Região')
plt.show()

vendas_produtos_regiao = data.groupby(['Region', 'Product Name'])['Units Sold'].sum().sort_values(ascending=False)
vendas_produtos_regiao

# Agrupar por região e produto, somar as unidades vendidas, e ordenar dentro de cada região
top_5_produtos_regiao = data.groupby(['Region', 'Product Name'])['Units Sold'].sum().groupby('Region', group_keys=False).apply(lambda x: x.sort_values(ascending=False).head(5))

print(top_5_produtos_regiao)

# Selecionar os 5 produtos mais vendidos em cada região
top_5_produtos_asia = vendas_produtos_regiao.loc['Asia'].head(5)
top_5_produtos_europe = vendas_produtos_regiao.loc['Europe'].head(5)
top_5_produtos_north_america = vendas_produtos_regiao.loc['North America'].head(5)

# Gráfico para os 5 produtos mais vendidos na Ásia
sns.barplot(x=top_5_produtos_asia.index, y=top_5_produtos_asia.values)
plt.title('Top 5 Produtos Mais Vendidos - Ásia')
plt.xticks(rotation=90)
plt.show()

# Gráfico para os 5 produtos mais vendidos na Ásia
sns.barplot(x=top_5_produtos_europe.index, y=top_5_produtos_europe.values)
plt.title('Top 5 Produtos Mais Vendidos - Europa')
plt.xticks(rotation=90)
plt.show()

# Gráfico para os 5 produtos mais vendidos na Ásia
sns.barplot(x=top_5_produtos_north_america.index, y=top_5_produtos_north_america.values)
plt.title('Top 5 Produtos Mais Vendidos - América do Norte')
plt.xticks(rotation=90)
plt.show()

vendas_metodo_regiao = data.groupby(['Region', 'Payment Method'])['Units Sold'].sum().sort_values(ascending=False)
vendas_metodo_regiao

# Selecionar a categoria mais vendida em cada região
principal_metodo_regiao = vendas_metodo_regiao.groupby('Region').head(1)

print(principal_metodo_regiao)

# Resetando o índice para transformar o MultiIndex em colunas
principal_metodo_regiao_reset = principal_metodo_regiao.reset_index()
principal_metodo_regiao_reset

# Criando o gráfico de barras com metodo usado por região
sns.barplot(x='Region', y='Units Sold', hue='Payment Method', data=principal_metodo_regiao_reset)
# Inclinando os rótulos do eixo X para melhor leitura
plt.title('Principal Metodo Por Regiao')
plt.show()

vendas_periodo_regiao = data.groupby(['Region', 'mes_ano'])['Units Sold'].sum().sort_values(ascending=False)
vendas_periodo_regiao

# Selecionar a categoria mais vendida em cada região
principal_periodo_regiao = vendas_periodo_regiao.groupby('Region').head(1)

print(principal_periodo_regiao)

principal_periodo_regiao_reset = principal_periodo_regiao.reset_index()
principal_periodo_regiao_reset

# Convertendo 'mes_ano' de Period para Timestamp (datetime)
vendas_por_regiao_mes['mes_ano'] = vendas_por_regiao_mes['mes_ano'].dt.to_timestamp()

# Criando o gráfico de linha
sns.lineplot(x='mes_ano', y='Units Sold', hue='Region', data=vendas_por_regiao_mes)

# Ajustando a visualização
plt.title('Padrão Sazonal das Vendas por Região')
plt.xticks(rotation=45)
plt.show()

total_vendas_regiao = data.groupby('Region')['Units Sold'].sum().sort_values(ascending=False)
total_vendas_regiao

sns.barplot(x=total_vendas_regiao.index, y=total_vendas_regiao.values)
plt.title('Total de Vendas por Região')
plt.show()
#

# Calculando a receita total (Unidades Vendidas * Preço Unitário)
data['Total Revenue'] = data['Units Sold'] * data['Unit Price']

sns.boxplot(x='Units Sold', data=data)
plt.title('Distribuição das Unidades Vendidas')
plt.show()

sns.boxplot(x='Total Revenue', data=data)
plt.title('Distribuição da Receita Total')
plt.show()

#calcular a receita total por categoria de produto
receita_total_categoria = data.groupby('Product Category')['Total Revenue'].sum().sort_values(ascending=False)
receita_total_categoria

# Criando o gráfico de barras para a receita total por categoria
sns.barplot(x=receita_total_categoria.index, y=receita_total_categoria.values)

# Ajustando a visualização
plt.title('Receita Total por Categoria')
plt.xticks(rotation=45)
plt.show()

# Agrupar por região e categoria de produto e somar a receita total
receita_regiao_categoria = data.groupby(['Region', 'Product Category'])['Total Revenue'].sum().sort_values(ascending=False)

# Resetando o índice para facilitar a visualização
receita_regiao_categoria_reset = receita_regiao_categoria.reset_index()

# Criando o gráfico de barras para receita por região e categoria
sns.barplot(x='Product Category', y='Total Revenue', hue='Region', data=receita_regiao_categoria_reset)

# Ajustando a visualização
plt.title('Receita Total por Categoria e Região')
plt.xticks(rotation=45)
plt.show()

