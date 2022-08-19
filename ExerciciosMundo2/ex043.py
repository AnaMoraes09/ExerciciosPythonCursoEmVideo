"""Desenvolva uma lógica que leia o peso e a altura de
uma pessoa, calcule seu Índice de Massa Corporal (IMC)
e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida"""

altura = float(input('Qual a sua altura em metros? '))
peso = float(input('Qual o seu peso? '))
imc = peso / (altura**2)
if imc < 18.5:
    print(f'Seu status é: abaixo do peso\nSeu IMC é de {round(imc, 2)}')
elif imc >= 18.5 and imc < 25:
    print(f'Seu status é: peso ideal\nSeu IMC é de {round(imc, 2)}')
elif imc >= 25 or imc < 30:
    print(f'Seu status é: SOBREPESO\nSeu IMC é de {round(imc, 2)}')
elif imc >= 30 <= 40:
    print(f'Seu status é: OBESIDADE\nSeu IMC é de {round(imc, 2)}v')
elif imc > 40:
    print(f'Seu status é: OBESIDADE MÓRBIDA\nSeu IMC é de {round(imc, 2)}')