""" A Confederação Nacional de Natação precisa de um programa
que leia o ano de nascimento de um atleta e mostre sua
categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER
"""

import datetime

date = datetime.date.today()
year = int(date.strftime("%Y"))
anoNascimento = int(input('Digite o ano do seu nascimento: '))
idade =  year - anoNascimento
if idade <= 9:
    print("Classificação: MIRIM")
elif idade <= 14:
    print("Classificação: INFANTIL")
elif idade <= 19:
    print("Classificação: JUNIOR")
elif idade <= 25:
    print("Classificação: SENIOR")
elif idade > 25:
    print("Classificação: MASTER")
print(f"O atleta tem {idade} anos")