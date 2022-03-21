# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado = float(input("Digíte a altura do quadrado: "))
area = lado * lado
dobroArea = area * 2

print("O dobro da área do quadrado(%.2f): %.2f" % (area, dobroArea))