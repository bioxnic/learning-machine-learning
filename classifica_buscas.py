import pandas as pd

# df stands for data_frame
df = pd.read_csv('busca.csv')
X_df = df[['home', 'busca', 'logado']]
Y_df = df['comprou']

Xdummies_df = pd.get_dummies(X_df)
Ydummies_df = Y_df
# transform to array
X = Xdummies_df.values
Y = Ydummies_df.values

porcentagem_treino = 0.9

tamanho_treino = int(porcentagem_treino * len(Y))
tamanho_teste = int(len(Y) - tamanho_treino)

treino_dados = X[:tamanho_treino]
treino_marcacoes = Y[:tamanho_treino]

teste_dados = X[-tamanho_teste:]
teste_marcacoes = Y[-tamanho_teste:]

from sklearn.naive_bayes import MultinomialNB

modelo = MultinomialNB()
modelo.fit(treino_dados, treino_marcacoes)

resultado = modelo.predict(teste_dados)
diferencas = resultado - teste_marcacoes

acertos = [d for d in diferencas if d == 0]
total_acertos = len(acertos)
total_elementos = len(teste_dados)
taxa_acerto = 100.0 * total_acertos / total_elementos

print(taxa_acerto)
print(total_elementos)