#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

a = float(input("Digite a altura em metros: "))
l = float(input("Digite a largura em metros: "))
area = a * l
print("A parede tem {}x{} e sua área é de {}m².".format(l, a, area))
tinta = area / 2
print("Para pintar essa parede serão necessários {}L de tinta.".format(tinta))
