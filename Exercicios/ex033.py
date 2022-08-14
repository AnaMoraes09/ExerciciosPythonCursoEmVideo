""" Faça um programa que leia três números e mostre qual é o maior e qual é o menor."""

num = int(input('Digite um números: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite mais um número: '))
maior = num
if num2 < num and num2 < num3:
    menor = num2
if num3 < num and num3 < num2:
    menor = num3
maior = num
if num2 > num and num3 > num2:
    maior = num2
if num3 > num and num3 > num2:
    maior = num3
print(f'O menor valor digitado foi: {menor}')
print(f'O maior valor digitado foi: {maior}')