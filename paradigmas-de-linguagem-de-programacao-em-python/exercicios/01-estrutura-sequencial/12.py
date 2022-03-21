# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input("Digíte a sua altura: "))
pesoIdeal = (72.7 * altura) - 58

print("Peso ideal para a altura %.2f: %.2fkg" % (altura, pesoIdeal))