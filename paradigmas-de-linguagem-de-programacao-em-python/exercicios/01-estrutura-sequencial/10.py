# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

celsius = float(input("Digíte a temperatura em graus celsius: "))
fahrenheit = celsius * 1.8 + 32

print("%.2f°C = %.2f°F" % (celsius, fahrenheit))