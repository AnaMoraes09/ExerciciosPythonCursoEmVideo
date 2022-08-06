"""Faça um programa que leia a largura e a altura  de uma parede em metros.
Calcule sua área e a quantidade de tinta para pinta-la, sabendo
que cada litro de tinta pinta uma área de 2m quadrados"""

largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))
area = largura*altura
tinta = area/2
print(f'Para uma área de {area}m², vamos precisar de {tinta}l de tinta')