#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salário = float(input("Digite o valor do seu salário: R$"))
aumento = salário * (15 / 100)
novo = salário + aumento
print("O seu novo salário será de R${:.2f}!".format(novo))