""" Faça um programa que leia o ano de nascimento de um jovem e
informe, de acordo com a sua idade, se ele ainda vai se alistar
ao serviço militar, se é a hora exata de se alistar ou se já passou
do tempo do alistamento. Seu programa também deverá mostrar o tempo
que falta ou que passou do prazo."""

import datetime

ano = int(input('Qual o seu ano de nascimento? '))
date = datetime.date.today()
year = int(date.strftime("%Y"))
idade = (ano - year) * -1
menor = (idade - 18) * -1
maior = (idade - 18)
if idade < 18:
    print(f'Você ainda vai se alistar\nDaqui {menor} anos')
if idade == 18:
    print('Esta na hora de se alistar ')
elif idade > 18:
    print(f'Já passou da hora de se alistar\nSe passaram {maior} anos do seu alistamento')