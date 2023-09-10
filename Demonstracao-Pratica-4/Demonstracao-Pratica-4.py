# Demonstração Prática 4 - Criação de Pipeline de Extração, Limpeza, Transformação e Enriquecimento de Dados

# Imports das bibliotecas usadas
import pandas as pd
from pandas.api.types import is_float_dtype
import sqlalchemy
from sqlalchemy import create_engine


def entrada_dados():
    print('Entrada dos dados')
    # Cria um dataframe com os dados do arquivo csv considerando '.' como separador de milhar
    df = pd.read_csv('producao_alimentos.csv', thousands='.')
    return df

def processamento_dado(df):
    print('Processamento dos dados')

    # Remove produtos com quantidade menor ou igual a 10
    df = df[df['quantidade_produzida_kgs'] > 10]

    # Verifica se todas os valores de 'quantidade_produzida_kgs' são maiores do que 10
    assert df['quantidade_produzida_kgs'].min() > 10

    # Converte 'valor_venda_medio' para float
    df['valor_venda_medio'] = df['valor_venda_medio'].astype(float)

    # Verifica se 'valor_venda_medio' é float
    assert is_float_dtype(df['valor_venda_medio'])

    # Define 'valor_venda_medio' com precisão de 2 casas decimais
    df['valor_venda_medio'] = df['valor_venda_medio'].round(2)

    # Cria coluna para margem de lucro com precisão de 2 casas decimais
    df['margem_lucro'] = ((df['receita_total'] / df['quantidade_produzida_kgs']) - df['valor_venda_medio']).round(2)
    # df['margem_lucro'] = df['margem_lucro'].round(2)

    # Verifica se a coluna 'margem_lucro' foi criada
    assert 'margem_lucro' in df.columns.values

    # Cria dicionário com nomes das colunas
    nomes_colunas_dict = {'quantidade_produzida_kgs': 'quantidade', 'valor_venda_medio': 'preco_medio'}

    # Renomeia algumas colunas do dataframe
    df = df.rename(columns=nomes_colunas_dict)

    # Verifica os nomes das colunas
    assert ['produto', 'quantidade', 'preco_medio', 'receita_total', 'margem_lucro'] in df.columns.values


def saida_dados(df):
    print('Saída dos dados')

    # Cria uma conexão com o banco de dados SQLite
    engine = create_engine('sqlite:///baseDeDados.db')

    # Salva o dataframe em uma tabela no banco de dados SQLite
    df.to_sql('produtos', engine, if_exists='replace', index=False)


def pipeline():
    try:
        print('Início da execução do Pipeline dos dados')

        df = entrada_dados()
        processamento_dado(df)
        saida_dados(df)

        print('Sucesso na execução do Pipeline dos dados')

    except BaseException:
        print('Falha na execução do Pipeline dos dados')

if __name__ == '__main__':
    pipeline()