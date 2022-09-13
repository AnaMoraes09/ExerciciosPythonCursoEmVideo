"""Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense."""

tupla = ('Palmeiras', 'Internacional', 'Flamengo', 'Fluminense', 'Corinthians', 'Athletico-PR', 'Atlético-MG', 'América-MG',
         'Goiás', 'Santos', 'Bragantino', 'Botafogo', 'São Paulo', 'Ceará', 'Fortaleza', 'Coritiba', 'Cuiabá', 'Avaí', 'Atlético-GO', 'Juventude')

print(f'Os 5 primeiros colocados são: {tupla[0:5]}\n')
print(f'Os 4 ultimos colocados são: {tupla[-4:]}\n')
print(f'Os times em ordem alfabetica é: {sorted(tupla)}\n', end=' ')
print('A Chapecoense está na série B')