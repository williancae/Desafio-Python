'''
Problema 2:
Dado um arquivo csv com delimitador ';' e com o seguinte cabeçalho: id;nome;telefone;idade.
Retorne uma lista com os registro ordenados por nome.
Exemplo de arquivo:
Id;nome;telefone;idade
1;João;43383832;28
2;Maria;43839322;32
.
.
.
N;Zzzz;99999999;12
'''

from pandas import read_csv
arq = read_csv('teste.csv', #arquivo CSV
               delimiter=';', #tipo de delimitador
               encoding='utf8' #caracteres especiais
               ).sort_values(by='nome') #ordenar pela coluna "nome"
arq.to_csv('order.csv', #criar um novo arquivo ordenado ou sobrescrever
           index=False #nao inserir no arquivo CSV os indexes default do Pandas
           )