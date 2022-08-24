""""Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão."""

pergunta1 = int(input('''Qual é o primeiro termo da sua PA?'''))
pergunta2 = int(input('''Qual é a razão da sua PA?'''))
decimo = pergunta1 + (10 - 1) * pergunta2
for i in range(pergunta1, decimo,pergunta2):
    print(i)