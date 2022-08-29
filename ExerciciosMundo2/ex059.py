n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))
opção = 0
while opção != 5:
    print('''Informe Oque Deseja Fazer:
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos Números
[ 5 ] Sair do Programa''')
    opção = int(input('Qual é a Sua Opção? '))
    if opção == 1:
        print('{}+{}={}'.format(n1, n2, n1+n2))
    elif opção == 2:
        print('{}x{}={}'.format(n1, n2, n1*n2))
    elif opção == 3:
        if n1 > n2:
            print('{} é Maior que {}.'.format(n1, n2))
        elif n1 == n2:
            print('{} e {} tem o Mesmo Valor'.format(n1, n2))
        else:
            print('{} é Maior que {}.'.format(n2, n1))
    elif opção == 4:
        print('Informe os Números Novamente: ')
        n1 = int(input('Primeiro Valor: '))
        n2 = int(input('Segundo Valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção Inválida. Tente Novamente!')
print('Fim do Programa! Volte Sempre!')