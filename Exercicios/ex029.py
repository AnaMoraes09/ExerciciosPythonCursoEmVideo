""" Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite."""


velocidade = int(input('Qual foi a velocidade do carro?'))
multa = (7 * (80 - velocidade)).__abs__()
if velocidade <= 80:
    print("")
else:
    print(f"""Você foi multado por ultrapassar o limite da via!\nA velocidade marcada foi de: {velocidade} Km/h\nO valor da multa é de: R${multa},00""")

"""Utilizei a função ABS para alterar o número negativo para positivo"""