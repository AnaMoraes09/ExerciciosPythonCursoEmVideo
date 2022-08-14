"""Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo."""
import math
import random

num = int(input('Digite um ângulo: '))
print(f'O cosseno de {num}° é: {math.cos(num)}\nO seno de {num}° é: {math.sin(num)}\nA tangente de {num}° é: {math.tan(num)}')