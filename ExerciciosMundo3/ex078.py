"""Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas
posições na lista."""
lista = []
for i in range(0, 5):
    numeros = int(input('Digite um numero: '))
    lista.append(numeros)
print('='*25)
print(f'Os valores digitados foram: {lista}')
print('='*25)
print(f'''O MAIOR numero digitado foi: {max(lista)}
E ele está na posição {lista.index(max(lista))} da lista''')
print('='*25)
print(f'''O MENOR numero digitado foi: {min(lista)}
E ele está na posição {lista.index(min(lista))} da lista''')
