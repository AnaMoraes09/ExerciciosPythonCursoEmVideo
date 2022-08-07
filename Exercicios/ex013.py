"""Faça um algoritmo que leia o salário de um funcionario
e mostre seu novo salario com 15% de aumento"""

salario = float(input('Digite seu salário atual: R$'))
aumento = salario*(15/100)
salarioComAumento = salario+aumento
print(f'Seu salário de R${salario}\ncom um aumento de 15% fica: R${round( salarioComAumento, 2 )}')

"""Utilizei o {round( salarioComAumento, 2 )} 
para colocar somente duas casas após a vírgula 
no resultado final"""