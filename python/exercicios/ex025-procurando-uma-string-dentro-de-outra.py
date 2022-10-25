#Faça um programa que leia o nome d euma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input("Qual é o seu nome completo? ")).strip()
print("Seu nome tem Silva? {}".format("SILVA" in nome.upper()))

'''n = "SILVA" in nome.upper()
if n == True
    else
    print("Seu nome tem Silva? Sim")
    elif
    print("Seu nome tem Silva? Não")'''