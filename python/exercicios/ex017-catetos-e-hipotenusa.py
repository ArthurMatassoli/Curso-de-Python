#Faça um programa que lia o comprimento do cateo oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot
co = float(input("Digite o valor do Cateto Oposto: "))
ca = float(input("Digite o valor do Cateto Adjacente: "))
hi = hypot(co, ca)
print("A hipotenusa: {:.2f}".format(hi))