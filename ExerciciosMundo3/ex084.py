dados = []
pessoas = []
cont = 0
pmaior = 0
pmenor = 0
while True:
    dados.append(str(input('Digite o nome: ')))
    dados.append(float(input('Digite o peso: ')))
    if len(pessoas) == 0:
        pmaior = pmenor = dados[1]
    else:
        if dados[1] > pmaior:
            pmaior = dados[1]
        if dados[1] < pmenor:
            pmenor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    cont += 1
    continuar = str(input("Deseja continuar? [S/N] ")).upper()
    if continuar in 'S':
        continue
    if continuar in 'N':
        break
    else:
        print('Você digitou algo errado. Tente novamente!')
        continuar = str(input("Deseja continuar? [S/N] "))

print("=" * 50)

print(f"Você cadastrou {len(pessoas)} pessoas.")
print(f"O maior peso foi de {pmaior:.2f}Kg. Peso de ", end='')
for p in pessoas:
    if p[1] == pmaior:
        print(f"[{p[0]}]", end=' ')
print()

print(f"O menor peso foi de {pmenor:.2f}Kg. Peso de ", end='')
for p in pessoas:
    if p[1] == pmenor:
        print(f"[{p[0]}]", end=' ')
