""" Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é
a condição de parada. No final, mostre quantos números foram digitados
e qual foi a soma entre eles (desconsiderando o flag)."""

numero = 0
contnum = 0
soma = 0
while numero != 999:
    soma += numero
    if numero != 999:
        numero = int(input('Digite um número: [999 para parar] '))
        contnum += numero != 999
print(f'Você digitou {contnum} numeros e a soma entre eles deu: {soma}')
print('FIM')
