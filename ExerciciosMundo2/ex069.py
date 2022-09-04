"""Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário
quer ou não continuar. No final, mostre:"""

c = homem = mulher = maior18 = 0
while True:
    se = ' '
    co = ' '
    print('='*10, 'CADASTRO', '='*10)
    nome = str(input('Digite um nome: ')).strip().upper()
    idade = int(input(f'Digite a idade de {nome} agora: '))
    if idade > 18:
        maior18 += 1
    while se not in 'MF':
        se = str(input(f'Digite o sexo de {nome} [M/F]: ')).strip().upper()[0]
    if se == 'M':
        homem += 1
    elif se == 'F':
        if idade < 20:
            mulher += 1
    while co not in 'SN':
        co = str(input('Você deseja continuar [S/N]? ')).strip().upper()[0]
    if co == 'N':
        break
print('='*10, 'FIM DO PROGRAMA', '='*10)
print(f'Você cadastrou {homem} homens. \nVocê cadastrou {maior18} pessoas maiores de 18 anos. \nVocê cadastrou {mulher} mulheres com menos de 20 anos.')