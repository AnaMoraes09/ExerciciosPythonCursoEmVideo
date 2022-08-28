"""Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos."""

lista = []

for peso in range(1, 6):
    lista.append(float(input(f'Qual é o peso da {peso}° pessoa?')))
print(f"""O maior peso é {max(lista)} KG
O menor peso é {min(lista)} KG""")