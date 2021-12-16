#1. Faça um programa que peça um valor monetário e diminua-o em 15%. Seu
#programa deve imprimir a mensagem “O novo valor é [valor]”.
valor = float(input ("Digite o valor monetário: "))
valor *= 0.85
print(f"O novo valor é [{valor}]")