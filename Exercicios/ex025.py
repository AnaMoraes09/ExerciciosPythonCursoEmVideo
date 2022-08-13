"""Crie um programa que leia um nome e
verifique se tem "Siva" no nome"""

nome = str(input('Digite um nome: ')).strip()
verifica = "SILVA" in nome.upper()
print(f'O nome apresenta "Silva"? {verifica}')