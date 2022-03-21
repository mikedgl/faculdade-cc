# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    # O produto do dobro do primeiro com metade do segundo.
    # A soma do triplo do primeiro com o terceiro.
    # O terceiro elevado ao cubo.

int1 = int(input("Digíte um número inteiro: "))
int2 = int(input("Digíte outro número inteiro: "))
real = float(input("Digíte um número real: "))

produto = int1 * 2 * (int2 / 2)
soma = int1 * 3 + real
cubo = real ** 3

print("O produto do dobro do primeiro com metade do segundo: %.2f" % produto)
print("A soma do triplo do primeiro com o terceiro: %.2f" % soma)
print("O terceiro elevado ao cubo: %.2f" % cubo)