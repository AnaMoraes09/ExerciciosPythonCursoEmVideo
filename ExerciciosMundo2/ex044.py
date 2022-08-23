"""Elabore um programa que calcule o valor a ser pago por um
produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal
– 3x ou mais no cartão: 20% de juros"""

compras = float(input('Qual foi o valor final das compras?'))
formaDepagamento = int(input(
'''[1] À vista dinheiro/cheque
[2] À vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão\n
Qual é a forma de pagamento?'''))

aVistaDinheiro= (((compras*10)/100)-compras)*-1
aVistaCartao = (((compras*5)/100)-compras)*-1
ateDuasVezes = compras
tresVezesOuMais = ((compras*20)/100)+compras

if formaDepagamento == 1:
    print(f'O valor da sua compra com 20% de desconto foi de R${compras}\nPara: R${round(aVistaDinheiro, 2)}')

if formaDepagamento == 2:
    print(f'O valor da sua compra com 5% de desconto foi de R${compras}\nPara: R${round(aVistaCartao, 2)}')

if formaDepagamento == 3:
    print(f'Você pagará o valor normal, que é R${compras}')

elif formaDepagamento == 4:
    parcelas = int(input('Em quantas vezes você deseja parcelar?'))
    print(f'''\nSua compra será parcelada em {parcelas}x de R${round(tresVezesOuMais/parcelas, 2)} COM JUROS
Sua compra de R${compras} vai custar no final R${tresVezesOuMais}''')