"""Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma
lista única que mantenha separados os valores pares e ímpares. No final,
mostre os valores pares e ímpares em ordem crescente."""
todos = []
listaPar = []
listaImpar = []
for i in range(1, 8):
    todos.append(int(input(f'Digite o {i}° valor: ')))
    for n in todos:
        if n % 2 == 0:
            listaPar.append(n)
            todos.clear()
        else:
            listaImpar.append(n)
            todos.clear()

print(f'Os valores pares digitados foram: {sorted(listaPar)}')
print(f'Os valores impares digitados foram: {sorted(listaImpar)}')
