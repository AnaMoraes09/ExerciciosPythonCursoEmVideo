""" Escreva um programa que pergunte a quantidade de Km percorridos por
um carro alugado e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado."""

km = float(input('Quantos Km seu carro percorreu? '))
dias = int(input('Quantos dias de aluguel você reservou? '))
preco = (dias*60) + (km*0.15)
print(f'Você pagará R${round(preco, 2)} no aluguel do carro')