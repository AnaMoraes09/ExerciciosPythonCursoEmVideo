""" Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder, mostrando
o total de vitórias consecutivas que ele conquistou no final do jogo."""
from random import randint
contv = 0
while True:
    print('\nPAR OU IMPAR\n')
    valor = int(input('Digite um valor: '))
    escolha = str(input('Par ou Ímpar? [P/I]'))
    computador = randint(0, 10)
    total = valor + computador
    if escolha in 'Pp':
        if total % 2 == 0:
            print(f'\nVocê jogou {valor} e o computador jogou {computador}, o total deu {total} DEU PAR')
            print('''Parabéns! Você ganhou\nContinue jogando...''')
            contv += 1
        else:
            print(f'\nVocê jogou {valor} e o computador jogou {computador}, o total deu {total} DEU IMPAR')
            print('Você PERDEU! FIM DE JOGO')
            break
    if escolha in 'Ii':
        if total % 2 != 0:
            print(f'\nVocê jogou {valor} e o computador jogou {computador}, o total deu {total} DEU IMPAR')
            print('''Parabéns! Você ganhou\nContinue jogando...''')
            contv += 1
        else:
            print(f'\nVocê jogou {valor} e o computador jogou {computador}, o total deu {total} DEU PAR')
            print('Você PERDEU! FIM DE JOGO')
            break
print(f'Você ganhou {contv} vezes ')

