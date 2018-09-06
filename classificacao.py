# eh gordinho? tem perninha curta? faz au au?
porco1 = [1, 1, 0]
porco2 = [1, 1, 0]
porco3 = [1, 1, 0]
cachorro1 = [1, 1, 1]
cachorro2 = [0, 1, 1]
cachorro3 = [0, 1, 1]

dados = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]

# 1 -> porco; -1 -> cachorro
marcacoes = [1, 1, 1, -1, -1, -1]

misterioso = [1, 1, 1]
misterioso2 = [1, 0, 0]
misterioso3 = [0, 0, 1]

testes = [misterioso, misterioso2, misterioso3]

marcacoes_teste = [-1, 1, -1]

from sklearn.naive_bayes import MultinomialNB

modelo = MultinomialNB()
modelo.fit(dados, marcacoes)
resultado = modelo.predict(testes)

print resultado

diferencas = resultado - marcacoes_teste
print diferencas

acertos = [d for d in diferencas if d == 0]
totalAcertos = len(acertos)
totalElementos = len(testes)
taxaAcertos = 100.0 * totalAcertos / totalElementos

print taxaAcertos