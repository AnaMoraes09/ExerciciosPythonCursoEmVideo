"""Crie um programa que leia o nome de uma cidade e diga se
ela começa ou não com "SANTO" """

cidade = str(input("Digite sua cidade:")).strip()
print(cidade[:5] == "Santo")

"""O programa irá determinar com falso se a primeira letra da palavra "Santo" 
estiver em minusculo, para resolver faremos assim:"""

cidade = str(input("Digite sua cidade:")).strip()
print(cidade[:5].upper() == "SANTO")