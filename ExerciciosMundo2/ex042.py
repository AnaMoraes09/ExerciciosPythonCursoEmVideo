"""Refaça o DESAFIO 35 dos triângulos,
 acrescentando o recurso de mostrar que tipo de triângulo será formado:
– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes"""

a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o terceiro segmento: '))
if a < b + c and b < a + c and c < b + a:
    print('Os segmentos PODEM formar um triangulo')
    if a == b == c:
        print("O triangulo é EQUILATERO")
    elif a == b or a == c or b == a or b == c or c == a or c == b:
        print("O triangulo é ISOSCELES")
    elif a != b != c:
        print("O triangulo é ESCALENO")
else:
    print('Os segmentos NÃO formam um triângulo')