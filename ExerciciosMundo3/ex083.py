"""Crie um programa onde o usuário digite uma expressão qualquer
que use parênteses. Seu aplicativo deverá analisar se a expressão
passada está com os parênteses abertos e fechados na ordem correta."""
formula = str(input('Digite uma expressão: '))
pilha = []
for i in formula:
    if i == '(':
        pilha.append('(')
    elif i == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão é válida')
else:
    print('Sua expressão não está válida')