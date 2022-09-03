"""Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while."""

pergunta1 = int(input('''Qual é o primeiro termo da sua PA?'''))
pergunta2 = int(input('''Qual é a razão da sua PA?'''))
termo = pergunta1
contador = 1
while contador <= 10:
    print(f'{termo} ->', end=' ')
    termo += pergunta2
    contador += 1
print("FIM", end=' ')