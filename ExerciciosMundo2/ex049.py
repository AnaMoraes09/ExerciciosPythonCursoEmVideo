""" Refaça o DESAFIO 9, mostrando a tabuada de um número que
o usuário escolher, só que agora utilizando um laço for."""

numeroPrincipal = int(input('Digite um numero que você queira saber a tabuada: '))

for i in range(1,11):
    print(f'{numeroPrincipal} X {i:2} = {numeroPrincipal*i}')