#Importando as bibliotecas 
import pandas as pd #biblioteca para ler arquivos xlsx(excel) - Pandas
import matplotlib.pyplot as plt #biblioteca para plotar gráficos - Matplotlib

#Lendo arquivo Excel
df = pd.read_excel (r'C:\Users\leona\Downloads\Vendas2019.xlsx')

#Criando arrays para receber os dados da planilha
meses = []
lucros = []

#Populando os arrays com informações da planilha
def obtemDados(df):
    for (i,row) in df.iterrows():
        mes = row['Data']
        lucro = row['Lucro']
        
        meses.append(mes)
        lucros.append(lucro)

#Executando os métodos criados acima
obtemDados(df)

#Definindo o eixo x e o eixo y
plt.bar(meses, lucros)

#Definindo label x do gráfico
plt.xlabel("Meses do ano")

#Definindo label y do gráfico
plt.ylabel("Valor em reais (R$)")

#Definindo Título do gráfico
plt.title("Lucro - 2019")

#Definindo tamanho padrão do gráfico
plt.rcParams['figure.figsize'] = (20,10)

#Plotando gráfico
plt.show()