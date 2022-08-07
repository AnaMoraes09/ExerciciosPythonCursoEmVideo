"""Escreva um programa que converta uma
temperatura digitada em °C e converta para °F"""

celsius = int(input('Digite a temperatura em °C: '))
fahrenheit = int(celsius * 9 / 5) + 32
print(f'A temperatura {celsius}°C em Fahrenheit é {fahrenheit}°F')
