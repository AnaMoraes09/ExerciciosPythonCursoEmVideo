import random

numComputador = random.randrange(0, 11)
numPessoa = 1
soma = 1

while numPessoa != numComputador:
    numPessoa = int(input('Digite um número de 0 á 10 que você acha que o computador escolheu: '))
    if numPessoa != numComputador:
        soma += 1
        print("Você não acertou, tente novamente")
    else:
        print(f"Parabéns!Você acertou, e precisou de {soma} tentativas para chegar no resultado")