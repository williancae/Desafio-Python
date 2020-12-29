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
		if k.upper() in 'NOME': #verifico se existe a chave nome (coloco o nome da chave em maiusculo pelo fato do Python ser case sensetive)
			if v not in lista: lista.append(v) #verifico se nao existe o valor na lista "not in" , caso nao exista adiciono a lista de nomes
print(lista)


#forma comprimida do algoritmo -- list compression
lista = list(set(humano['nome'] for humano in galera if 'nome' in humano))
print(lista)