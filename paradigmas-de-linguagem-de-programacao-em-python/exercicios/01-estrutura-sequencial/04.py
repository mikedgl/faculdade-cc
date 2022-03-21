# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota1 = float(input("Digíte a primeira nota: "))
nota2 = float(input("Digíte a segunda nota: "))
nota3 = float(input("Digíte a terceira nota: "))
nota4 = float(input("Digíte a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print("Média das quatro notas bimestrais: %.2f" % media)