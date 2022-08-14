""" Escreva um programa que pergunte o salário de um funcionário e calcule
o valor do seu aumento. Para salários superiores a R$1250,00, calcule um
aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%."""

salario = float(input('Digite o valor do seu salário: '))
maiorSalario = (salario/100 * 10) + salario
menorSalario = (salario/100 * 15) + salario
if salario > 1250:
    print(f'Você teve um aumento de 10%! Seu salário atual é R${round(maiorSalario, 2)}')
if salario <= 1250:
    print(f'Você teve um aumento de 15%! Seu salário atual é R${round(menorSalario, 2)}')