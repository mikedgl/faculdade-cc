#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).


tamanhoMb = float(input("Digíte o tamanho do arquivo para download(Mb): "))
velocidadeMbps = float(input("Digíte a velocidade do link da internet(Mbps): "))

tempo = tamanhoMb / velocidadeMbps
minutos = tempo / 60

print("O tempo aproximado de download do arquivo usando este link: %.2f minutos" % minutos)