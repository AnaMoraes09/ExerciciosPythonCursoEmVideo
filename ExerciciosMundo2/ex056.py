""" Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo, qual é o nome do homem
mais velho e quantas mulheres têm menos de 20 anos."""

soma = 0
lista = []
maioridadehomem = 0
nomedomaisvelho = ''
mulher20 = 0


for i in range(1, 5):
    print(f'----{i}° PESSOA-----')
    nome = str(input(f"Qual o nome da pessoa?"))
    idade = (int(input(f"Qual idade da  pessoa?")))
    sexo = str(input(f"Qual o sexo [M/F] da  pessoa?")).upper()
    soma += idade
    if i == 1 and sexo == 'M':
        maioridadehomem = idade
        nomedomaisvelho = nome
    if sexo == "M" and idade > maioridadehomem:
        maioridadehomem = idade
        nomedomaisvelho = nome
    if sexo == "F" and idade < 20:
        mulher20 += 1

lista.append(idade)
mediaidade = soma/4

print(f"""\nA Media de idade do grupo é: {mediaidade}
O homem mais velho tem {maioridadehomem} anos e se chama {nomedomaisvelho.capitalize()}
Ao todo são {mulher20} mulheres com menos de 20 anos""")

