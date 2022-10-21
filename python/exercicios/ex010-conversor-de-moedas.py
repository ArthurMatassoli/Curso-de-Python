#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

d = float(input("Digite o valor em reais a ser convertido: R$"))
dolar = d / 3.27
print("Você poderá comprar US${:.2f} doláres!".format(dolar))
