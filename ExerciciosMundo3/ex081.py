""" Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista."""
lista = []
cont = 0
while True:
    numero = int(input('Digite um valor: '))
    lista.append(numero)
    cont += 1
    parada = str(input('Deseja continuar? [S/N] '))
    if parada in 'Ss':
        continue
    if parada in 'Nn':
        break
    else:
        print('Você pode ter digitado algo errado. Tente novamente')
        parada = str(input('Deseja continuar? [S/N] '))
print('='*25)
print(f'Foram digitados {cont} numeros')
print('='*25)
lista.sort(reverse=True)
print(f'Os valores digitados foram {lista}')
print('='*25)
if 5 in lista:
    print('O valor 5 ESTÁ presente na lista')
else:
    print('O valor 5 NÃO está presente na lista')