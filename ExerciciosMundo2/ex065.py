"""Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior
e o menor valores lidos. O programa deve perguntar ao usuário
se ele quer ou não continuar a digitar valores."""

lista = []
numero = 0
continuar = 'S'
contnum = 0
soma = 0
while continuar in 'Ss':
    numero = int(input('Digite um número: '))
    soma += numero
    contnum += 1
    continuar = str(input('Você deseja continuar? [S/N]')).upper()
    lista.append(numero)
media = soma/contnum
print(f'''\nVocê digitou {contnum} números e a média foi de {round(media, 2)}
O maior numero digitado foi {max(lista)} e o menor número digitado foi {min(lista)}''')
