""" Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais."""

tupla = ('CACHORRO', 'GATO', 'PASSARINHO', 'BOI', 'VACA', 'LEOPARDO', 'MACACO', 'PEIXE', 'SAPO', 'COBRA')

for n in tupla:
    print(f'\nNa palavra {n.upper()} temos ',  end='')
    for letra in n:
        if letra.lower() in 'aeiou':
            print(letra, end='')
