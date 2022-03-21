'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
Salário bruto.
Quanto pagou ao INSS.
Quanto pagou ao sindicato.
O salário líquido.
Salcule os descontos e o salário líquido, conforme a tabela abaixo:
     + Salário Bruto : R$
     - IR (11%) : R$
     - INSS (8%) : R$
     - Sindicato ( 5%) : R$
     = Salário Liquido : R$
'''

valorHora = float(input("Valor por hora: "))
horasTrabalhadas = int(input("Horas trabalhadas no mês: "))

salarioBruto = valorHora * horasTrabalhadas

impostoRenda = salarioBruto * 0.11
inss = salarioBruto * 0.08
sindicato = salarioBruto * 0.05

salarioLiquido = salarioBruto - impostoRenda - inss - sindicato

print("+ Salário Bruto : %.2f R$" % salarioBruto)
print("- IR (11%%): %.2f R$" % impostoRenda)
print("- INSS (8%%): %.2f R$" % inss)
print("- Sindicato (5%%): %.2f R$" % sindicato)
print("= Salário Líquido: %.2f R$" % salarioLiquido)