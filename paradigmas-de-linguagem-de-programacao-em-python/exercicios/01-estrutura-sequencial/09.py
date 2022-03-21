# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

fahrenheit = float(input("Digíte a temperatura em graus fahrenheit: "))
celsius = 5 * ((fahrenheit-32) / 9)

print("%.2f°F = %.2f°C" % (fahrenheit, celsius))