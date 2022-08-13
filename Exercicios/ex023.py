"""Faça um programa que mostre de 0 a 9999 e mostre na tela cada um
dos dígitos separados"""

num = int(input('Digite um número de 0 a 9999: '))
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10

print(f"""Unidade: {unidade}
Dezena: {dezena}
Centena: {centena}
Milhar: {milhar}""")