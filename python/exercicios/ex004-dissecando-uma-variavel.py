#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ela.

n = input("Digite algo: ")
print('O tipo primitivo desse valor é', type(n))
print("O objeto é um número? {}".format(n.isnumeric()))
print("O objeto é alphanúmerico? {}".format(n.isalnum()))
print("O objeto está todo em letras minúsculas? {}".format(n.islower()))
print("O objeto está todo em letras maiúsculas? {}".format(n.isupper()))
print("O objeto é um número decimal? {}".format(n.isdecimal()))
print("O objeto é um espaço? {}".format(n.isspace()))