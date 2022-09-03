"""Melhore o DESAFIO 61, perguntando para o usuário se ele quer
mostrar mais alguns termos. O programa encerrará quando ele disser
que quer mostrar 0 termos."""

pergunta1 = int(input('''Qual é o primeiro termo da sua PA?'''))
pergunta2 = int(input('''Qual é a razão da sua PA?'''))
termo = pergunta1
contador = 1
total = 0
pergunta3 = 10
while pergunta3 != 0:
    total = total + pergunta3
    while contador <= total:
        print(f'{termo} ->', end=' ')
        termo += pergunta2
        contador += 1
    print("PAUSA", end=' ')
    pergunta3 = int(input("\nQuantos termos você quer mostrar mais? "))
print('FIM')

