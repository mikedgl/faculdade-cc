# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math

raio = float(input("Digíte o raio do círculo: "))
area = math.pi * (raio * raio)

print("A área de um círculo com o raio de %.2f: %.2f" % (raio, area))