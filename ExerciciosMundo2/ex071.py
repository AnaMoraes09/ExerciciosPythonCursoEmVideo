"""Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues. """

n = int(input('Digite o valor a ser sacado: '))
lista = [50, 20, 10, 1]
print('Serão necessárias ', end='')
saldo = n
i = 0
while i <= 3:
    valor = lista[i]
    qnota = saldo // valor
    print(f'{qnota} notas de R${lista[i]}', end='')
    if i < 3:
        print(', ', end='')
    saldo -= (qnota * lista[i])
    i += 1
    if saldo == 0:
        break
print(' para compor o valor total do seu saque.', end='')
