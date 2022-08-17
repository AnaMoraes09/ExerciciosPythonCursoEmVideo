"""Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:"""

primeiroNumero = int(input('Digite o primeiro número: '))
segundoNumero = int(input('Digite o segundo número: '))

if primeiroNumero > segundoNumero:
    print("O primeiro valor é maior")
elif segundoNumero > primeiroNumero:
    print("O segundo valor é maior")
else:
    print('Não existe valor maior, os dois são iguais')