"""Crie um programa que leia algo pelo teclado e mostre na tela
o seu tipo primitivo e todas as informações possiveis sobre ela"""

frase = input('Digite algo: ')
print(f'O tipo do valor é: {type(frase)}')
print(f'É numerico? {frase.isnumeric()}')
print(f'É decimal?  {frase.isdecimal()}')
print(f'Tem título? {frase.istitle()}')
print(f'Todos os caracteres são maiusculos? {frase.isupper()}')
print(f'Tem espaço? {frase.isspace()}')
print(f'Tem somente letras juntas? {frase.isalpha()}')
print(f'Todos os caracteres são minusculos? {frase.islower()}')
