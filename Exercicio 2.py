#Faça um programa que leia a validade das informações:
#a. Idade: entre 0 e 150;
#b. Salário: maior que 0;
#c. Sexo: M, F ou Outro;
#O programa deve imprimir uma mensagem de erro para cada informação
#inválida.

idade = int(input("Idade entre 0 e 150:"))
while 150<idade<0:
    idade = int(input("Erro. Digite Idade entre 0 e 150: "))

salario = int(input("Salário: maior que 0: "))
while salario<0 or float(salario)<0:
    idade = int(input("Erro. Digite Salário: maior que 0: "))

sexo = int(input("Sexo: M, F ou Outro: "))
while sexo != "M" and sexo != "F" and sexo!="Outro":
    sexo = int(input("Erro. Digite Sexo: M, F ou Outro: "))