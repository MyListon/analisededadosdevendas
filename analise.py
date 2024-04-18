import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dados = ler_dados('dados_venda.csv')
def ler_dados(dados):
    """Função para ler os dados do arquivo CSV"""
    return pd.read_csv('dados_venda.csv')

def analisar_vendas(dados):
    """Função para realizar análises estatísticas básicas"""
    total_vendas = dados['Valor'].sum()
    media_vendas_por_mes = dados.groupby(pd.to_datetime(dados['Data']).dt.to_period('M'))['Valor'].mean()
    produtos_mais_vendidos = dados['Produto'].value_counts().head(5)
    return total_vendas, media_vendas_por_mes, produtos_mais_vendidos

def visualizar_dados(dados):
    """Função para gerar gráficos e visualizações"""
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Produto', y='Valor', data=dados, estimator=sum)
    plt.title('Total de Vendas por Produto')
    plt.xlabel('Produto')
    plt.ylabel('Total de Vendas')
    plt.xticks(rotation=45)
    plt.show()

    plt.figure(figsize=(10, 6))
    dados['Data'] = pd.to_datetime(dados['Data'])
    dados['Mês'] = dados['Data'].dt.strftime('%b')
    sns.lineplot(x='Mês', y='Valor', data=dados, estimator=sum)
    plt.title('Tendência de Vendas ao Longo do Tempo')
    plt.xlabel('Mês')
    plt.ylabel('Total de Vendas')
    plt.show()

def identificar_tendencias(dados):
    """Função para identificar tendências e padrões nos dados de vendas"""
    # Aqui você pode adicionar código para identificar sazonalidade de vendas, correlações entre produtos, etc.
    pass

def exportar_resultados(resultados):
    """Função para exportar os resultados da análise"""
    # Aqui você pode adicionar código para exportar os resultados para arquivos ou relatórios
    pass

if __name__ == "__main__":
    # Ler os dados do arquivo CSV
    dados = ler_dados('dados_vendas.csv')

    # Realizar análises estatísticas básicas
    total_vendas, media_vendas_por_mes, produtos_mais_vendidos = analisar_vendas(dados)
    print('Total de Vendas:', total_vendas)
    print('Média de Vendas por Mês:\n', media_vendas_por_mes)
    print('Produtos Mais Vendidos:\n', produtos_mais_vendidos)

    # Gerar gráficos e visualizações
    visualizar_dados(dados)

    # Identificar tendências e padrões nos dados de vendas
    identificar_tendencias(dados)

    # Exportar os resultados da análise
    exportar_resultados({'Total de Vendas': total_vendas, 'Média de Vendas por Mês': media_vendas_por_mes, 'Produtos Mais Vendidos': produtos_mais_vendidos})