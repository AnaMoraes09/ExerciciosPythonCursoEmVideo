"""Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras
que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre
o conteúdo das três listas geradas."""
lista = []
pares = []
impar = []
while True:
    numero = int(input('Digite um valor: '))
    lista.append(numero)
    parada = str(input('Deseja continuar? [S/N] '))
    if parada in 'Ss':
        continue
    if parada in 'Nn':
        break
    else:
        print('Você pode ter digitado algo errado. Tente novamente')
        parada = str(input('Deseja continuar? [S/N] '))
for i in lista:
    if i % 2 == 0:
        pares.append(i)
    else:
        impar.append(i)
print('='*25)
print(f'''Os valores listados foram: {lista}
Os valores pares são: {pares}
Os valores impares são: {impar}''')
