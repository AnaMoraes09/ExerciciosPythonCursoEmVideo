"""Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens
de até 200Km e R$0,45 parta viagens mais longas."""

viagem = int(input('Digite a distância em Km de uma viagem: '))
viagemCurta = viagem * 0.50
viagemLonga = viagem * 0.45
if viagem <= 200:
    print(f'O valor da passagem é de: R${viagemCurta}')
else:
    print(f'O valor da passagem é de: R${viagemLonga}')