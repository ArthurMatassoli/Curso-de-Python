print("Olá, Mundo!")
print(7 + 4) = 11
print("7" + "4") = 74
print("Olá", 5) = Olá 5

====================================================================================================
Variáveis
nome = Arthur
idade = 19
peso = 100

print(nome, idade, peso) = Arthur 19 100

nome = imput("Qual seu nome?")
idade = imput("Qual sua idade?")
peso = imput("Quantos anos voçê tem?")

print(nome, idade, peso)

====================================================================================================

Tipos Primitivos e Saída de Dados

int = 7, -4, 0, 9875
float = 4.5, 0.0076, -15.223, 7.0
bool = True, False
str = 'Olá', '7.5', ' '

print('A soma vale', s)
print('A soma vale {}'.format(s))

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
s = n1 + n2
print("A soma vale {}.".format(s))

====

print("O objeto é um número? {}".format(n.isnumeric()))
print("O objeto é alphanúmerico? {}".format(n.isalnum()))
print("O objeto está todo em letras minúsculas? {}".format(n.islower()))
print("O objeto está todo em letras maiúsculas? {}".format(n.isupper()))
print("O objeto é um número decimal? {}".format(n.isdecimal()))
print("O objeto é um espaço? {}".format(n.isspace()))

====================================================================================================

Operadores Aritméticos                      Ordem de precedência

+ = adição          ** = potência           1º = ()
- = subtração       // = divisão inteira    2º = **
*  = multiplicação  % = resto da divisão    3º = * / // %
/ =  divisão                                4º = + -

5 + 2 == 7          5 ** 2 == 25        5 + 3 * 2 == 11
5 - 2 == 3          5 // 2 == 2         3 * 5 + 4 == 31
5 * 2 == 10         5 % 2 == 1          3 * (5 + 4) ** 2 == 243
5 / 2 == 2.5

print("=" * 20)
print("Prazer em te conhecer Arthur {:=^20}!".format(nome))

=====

n1 = int(input("Um valor: "))
n2 = int(input("Outro Valor: "))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
#print("A soma vale {}".format(n1+n2))
print("A soma é {}, o produto é {} e a divisão é {:.3f}".format(s, m , d), end=" ")
print("Divisão inteira {} e potência {}".format(di, e))