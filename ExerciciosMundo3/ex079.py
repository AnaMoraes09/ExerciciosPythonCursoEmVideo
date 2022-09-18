"""Crie um programa onde o usuário possa digitar vários valores
numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro,
ele não será adicionado. No final, serão exibidos todos os valores únicos
digitados, em ordem crescente."""
lista = []
while True:
    numeros = int(input('Digite um valor: '))
    lista.append(numeros)
    resultadolista = []
    for elemento in lista:
        if elemento not in resultadolista:
            resultadolista.append(elemento)
            resultadolista.sort()
    con = str(input('Deseja continuar? [S/N]'))
    if con in 'Ss':
        continue
    if con in 'Nn':
        break
    else:
        print('Você pode ter digitado algo errado. Tente novamente')
        con = str(input('Deseja continuar? [S/N]'))
print('='*25)
print(f'Os valores digitados foram: {resultadolista}')