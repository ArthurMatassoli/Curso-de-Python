#Crie um programa que leia o nome completo de uma pessoa e mostre:
#- O nome com todas as letras maiúsculas e minúsculas.
#- Quantas letras ao todo (sem considerar espaços).
#- Quantas letras tem o primeiro nome.

nome = input("Qual é o seu nome completo? ").strip()
print("Seu nome em letras maiúsculas: {}".format(nome.upper()))
print("Seu nome em letras minúsculas: {}".format(nome.lower()))
print("Seu nome tem ao todo {} letras.".format(len(nome) - nome.count(" ")))
separa = nome.split()
print("Seu primeiro nome é {} e ele tem {} letras.".format(separa[0], len(separa[0])))
