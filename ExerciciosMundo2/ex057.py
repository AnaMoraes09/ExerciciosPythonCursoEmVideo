
sexo = str(input('Qual o seu sexo [M]/[F]?')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Por favor selecione o dado corretamente: ')).strip().upper()[0]
print('Tudo certo')