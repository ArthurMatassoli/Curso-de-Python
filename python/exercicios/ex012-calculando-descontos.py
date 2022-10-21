#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

prod = float(input("Digite o valor do produto: R$"))
desc = prod * (5 / 100)
valor = prod - desc
print("O Valor do produto com 5% de desconto é: R${:.2f}".format(valor))

