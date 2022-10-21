#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

v = float(input("Digite a distância em metros: "))
cm = v * 100
dm = v * 1000
print("O valor convertido em Centímetros é = {}cm!\nO valor convertido em Milímetros é = {}dm!".format(cm, dm))