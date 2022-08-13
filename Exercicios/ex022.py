"""Crie um programa que leie o nome de uma pessoa e mostre
- O nome com todas as letras maiusculas
- O nome com todas as letras minusculas
- Quantas letras tem o primeiro nome
- Quantas letras tem ao todo sem considerar espaços
"""

nome = str(input("Digite um nome: "))
dividir = nome.split()
primeiroNome = dividir[0]
branco = nome.replace(" ","")
print(f"""O nome com todas as letras maiusculas é: {nome.upper()}
O nome com todas as letras minusculas é: {nome.lower()}
Seu primeiro nome tem: {len(primeiroNome)} letras
O nome tem um total de: {len(branco)} letras""")


