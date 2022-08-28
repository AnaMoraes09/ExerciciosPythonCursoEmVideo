"""Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade
e quantas já são maiores."""

import datetime

data = datetime.date.today()
ano = int(data.strftime("%Y"))

#Essas duas variaveis servem para acumular resultados
totmaior = 0
totmenor = 0

for i in range(1,8):
    nascimento = int(input(f'Digite o {i}° ano de nascimento: '))
    idade = ano - nascimento
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f'Temos {totmaior} pessoas maiores de idade e {totmenor} pessoas menores de idade')