"""Faça um programa que leia um número qualquer e mostre o seu fatorial."""
import math
numero = int(input("""Digite um numero para calcular seu fatorial: """))
c = numero
while c >0:
    print(f'{c}', end=' ')
    if c > 1:
        print('x', end=' ')
    else:
        print('=', end=' ')
    c -= 1
print(math.factorial(numero), end=' ')