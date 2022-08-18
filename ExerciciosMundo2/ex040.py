"""Crie um programa que leia duas notas de um aluno e
calcule sua média, mostrando uma mensagem no
final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO"""

nota1 = float(input('Qual foi a sua nota em matemática 1? '))
nota2 = float(input('Qual foi a sua nota em matemática 2? '))
media = (nota1 + nota2) / 2
if media < 5:
    print('Você foi REPROVADO! Estude mais!')
elif media > 7:
    print('Você foi APROVADO! Parabéns!')
elif media >= 5 and media < 7:
    print('Você ficou de RECUPERAÇÃO! Ainda tem chance de passar!')