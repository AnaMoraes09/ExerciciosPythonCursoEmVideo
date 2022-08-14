"""Faça um programa que leia o comprimento do cateto oposto e do adjacente de um
triangulo retangulo e calcule o valor da hipotenusa"""
import math
num1= int(input('Digite o cateto maior: '))
num2 = int(input('Digite o cateto menor: '))
hipotenusa = math.hypot(num1 , num2)
print(f'A hipotenusa  é: {hipotenusa}')