"""Crie um programa que faça o computador jogar Jokenpô com você."""

from random import randint

lista = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual é a sua jogada?\n'))

if computador == 0:
    print('Computador jogou Pedra')
    if jogador == 0:
        print('Jogador jogou Pedra')
        print('-=' * 20)
        print('EMPATE')
    if jogador == 1:
        print('Jogador jogou Papel')
        print('-=' * 20)
        print('O JOGADOR VENCEU')
    if jogador == 2:
        print('Jogador jogou Tesoura')
        print('-=' * 20)
        print('O COMPUTADOR VENCEU')
elif computador == 1:
    print('Computador jogou Papel')
    if jogador == 0:
        print('Jogador jogou Pedra')
        print('-=' * 20)
        print('O COMPUTADOR VENCEU')
    if jogador == 1:
        print('Jogador jogou Papel')
        print('-=' * 20)
        print('EMPATE')
    if jogador == 2:
        print('Jogador jogou Tesoura')
        print('-=' * 20)
        print('O JOGADOR VENCEU')
else:
    print('Computador jogou Tesoura')
    if jogador == 0:
        print('Jogador jogou Pedra')
        print('-=' * 20)
        print('O JOGADOR VENCEU')
    if jogador == 1:
        print('Jogador jogou Papel')
        print('-=' * 20)
        print('O COMPUTADOR VENCEU')
    if jogador == 2:
        print('Jogador jogou Tesoura')
        print('-=' * 20)
        print('EMPATE')