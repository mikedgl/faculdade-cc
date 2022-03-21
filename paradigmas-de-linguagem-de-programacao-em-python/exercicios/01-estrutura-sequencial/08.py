# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valorHora = float(input("Valor por hora: "))
horasTrabalhadas = int(input("Horas trabalhadas no mês: "))

salario = valorHora * horasTrabalhadas

print("Salário total no mês: %.2f" % salario)