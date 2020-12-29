'''
Problema 1:
Dado uma lista de dicionários (chave/valor) Python, verifique se existe a chave 'nome',
e caso exista, salve o valor dessa chave em uma segunda lista,
de modo que não haja repetição de valores na segunda lista.
'''
lista = list()
galera = [{'nome':'willian', 'idade':21}, {'nome':'murilo', 'idade':23},
          {'nome':'greg','idade':38}, {'nome':'miguel', 'idade':18},
          {'nome':'willian', 'idade':21}, {'nome':'Gabriel', 'idade':21}]

for humano in galera:
	for k,v in humano.items():
		if k.lower() == 'nome': #verifico se existe a chave nome (coloco o nome da chave em maiusculo pelo fato do Python ser case sensetive)
			if v not in lista: lista.append(v) #verifico se nao existe o valor na lista "not in" , caso nao exista adiciono a lista de nomes
print(lista)
'''
Explicação:
° no primeiro "for" ele percorre todos os indices da lista, e devolve o "dict" dicionario de cada posição
° o segundo "for" ele pega o dicionario recebido no primeiro "for" e devolve  a chave e o valor dele
° o primeiro "if" compara se o nome da chave é igual a "nome", caso seja verdadeira execute o que esta dentro
° o sugundo "if" verifica se existe o valor da chave exieste na lista de nomes, se o valor ainda nao existe na lista ele adiciona a lista "lista"
'''

#forma comprimida do algoritmo -- list compression
lista = list(set(humano['nome'] for humano in galera if 'nome' in humano))
print(lista)

'''
Explicação:
° Utilizo o metodo "set" para retirar os valores repetidos na lista
° O "for" é utilizado para percorrer a lista de dicionarios e fazer as comparações
'''
