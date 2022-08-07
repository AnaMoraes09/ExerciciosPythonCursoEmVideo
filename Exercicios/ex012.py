""" Faça um algoritmo que leia o preço de um produto
e mostre seu novo preço com 5% de desconto"""

produto = float(input('Digite o preço do seu produto: R$'))
desconto = produto*(5/100)
produtoComDesconto = produto-desconto
print(f'O desconto de 5% em cima do seu produto é de R${round(desconto, 2)}\nO valor com o desconto fica: R${round(produtoComDesconto, 2)}')
