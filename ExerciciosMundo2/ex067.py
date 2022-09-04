""" Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo."""


while True:
    numeroPrincipal = int(input('Digite um numero que você queira saber a tabuada: '))
    if numeroPrincipal < 0:
        break
    for i in range(1,11):
        print(f'{numeroPrincipal} X {i:2} = {numeroPrincipal*i}')
print('PROGRAMA ENCERRADO')