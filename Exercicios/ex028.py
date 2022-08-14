"""Escreva um programa que faça o computador “pensar” em um número inteiro entre
0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu"""

import random

numComputador = random.randrange(0,6)
numPessoa = int(input('Digite um número de 0 á 5 que você acha que o computador escolheu: '))
if numPessoa == numComputador:
    print("\nParabéns! Você acertou!")
else:
    print(f'\nVocê não acertou! tente novamente.\nO número que o computador escolheu foi: {numComputador}')