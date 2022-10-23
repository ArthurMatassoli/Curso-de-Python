#Escreva um programa que converta uma temperatura digitada em ºC e converta para °F.

c = float(input("Digite a temperatura em ºC: "))
f = (c * 1.8) + 32
print("A temperatura de {}ºC corresponde a {}ºF!".format(c, f))
