"""Faça um programa que calcule a soma entre todos os números
que são múltiplos de três e que se encontram no intervalo de 1 até 500."""

lista = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        lista = lista + i
print(f"A soma dos valores é {lista}")