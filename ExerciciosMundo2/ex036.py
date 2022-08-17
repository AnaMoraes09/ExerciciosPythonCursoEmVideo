"""Escreva um programa para aprovar o empréstimo bancário para
a compra de uma casa. Pergunte o valor da casa, o salário do comprador
e em quantos anos ele vai pagar. A prestação mensal não pode exceder
30% do salário ou então o empréstimo será negado."""

valorCasa = int(input('Digite o valo da casa que deseja comprar: '))
salario = float(input('Digite o valor do seu salario: '))
previsaoDePagamentoEmAnos = int(input('Digite em quantos anos você deseja pagar a casa: '))
prestacao = valorCasa / (previsaoDePagamentoEmAnos * 12)
minimo = salario * 30 / 100
print(f'Para pagar uma casa de {round(valorCasa, 2)} em {previsaoDePagamentoEmAnos} anos')
print(f'A prestação será de: R${round(prestacao, 2)}')
if prestacao <= minimo:
    print('Empréstimo CONCEBIDO')
else:
    print('Empréstimo NEGADO')