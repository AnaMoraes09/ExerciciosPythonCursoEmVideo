"""Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares """

tupla = (int(input('Digite um valor: ')),
         int(input('Digite outro valor: ')),
         int(input('Digite mais um valor: ')),
         int(input('Digite o ultimo valor: ')))
print("="*40)
if 9 in tupla:
    print(f'O número 9 foi digitado e apareceu {tupla.count(9)} vezes')
else:
    print('O numero 9 NÃO foi digitado')
print("="*40)
if 3 in tupla:
    print(f'O primeiro numero 3 aparece na posição {tupla.index(3)}')
else:
    print("O número 3 NÃO foi digitado")
print("="*40)
print(f'Os valores pares digitados foram: ')
for n in tupla:
    if n % 2 == 0:
        print(n,end=' ')
