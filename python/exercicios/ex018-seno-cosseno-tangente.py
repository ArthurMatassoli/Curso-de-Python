#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import cos, tan, sin, radians
ang = int(input("Digite o ângulo que você deseja: "))
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print("O ângulo de {}º tem o SENO de {:.2f}".format(ang, sen))
print("O ângulo de {}º tem o COSSENO de {:.2f}".format(ang, cos))
print("O ângulo de {}º tem a TANGEnTE de {:.2f}".format(ang, tan))
