#Faça um programa que olhe todos os itens de uma lista e diga quantos deles são pares.
lista = [1,2,3,4,5,6,7,8,9,10]
pares=[]
for item in lista:
    if int(item)%2==0:
        pares.append(item)
print(pares)

