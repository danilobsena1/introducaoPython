print("\t LAÇOS DE REPETIÇÃO")

for x in range(100):
    print(x) # serão exibidos valores de 0 a 99

# ----------------------------------------------------
print("Exibidos valores de 1 a 100")

for x in range(1, 101):
    print(x) # serão exibidos valores de 1 a 100

# ----------------------------------------------------

print("IMPRIMINDO APENAS NUMEROS PRIMOS")
# O número somente é primo quando é dividido por 1 e por ele mesmo.

numero = int(input("Digite um número: "))
div = 0

for x in range(1, numero+1):
    resto = numero % x  # A variavel resto irá receber o resto da divisão
    print("Divisor: {divisor} - Resto: {resto}".format(divisor=x, resto=resto))
    if resto == 0:
        div = div + 1 # a variavel div irá acumular o valor total de zeros.

if div == 2: # Se o total de zeros for igual a dois, execute o código abaixo
    print("Número {} é primo".format(numero))
else: # Senão execute a linha de código abaixo
    print("Número {} não é impar".format(numero))

# ------------------------------------------------------------------------
#EXIBINDO OS NÚMEROS PRIMOS entre 1 e 100
#
# for numero in range(101):
#     div = 0
#     for x in range(1, numero+1): # numero+1 para que o ultimo numero tb seja contado.
#         resto = numero % x  # A variavel resto irá receber o resto da divisão
#         if resto == 0:
#             div = div + 1 # a variavel div irá acumular o valor total de zeros.
#
#     if div == 2: # Se o total de zeros for igual a dois, execute o código abaixo
#         print(numero)

# ------------------------------------------------------------------------
# valor = int(input("Entre com o valor: "))
# for numero in range(valor+1):
#     div = 0
#     for x in range(1, numero+1):
#         resto = numero % x
#         if resto == 0:
#             div = div + 1
#     if div == 2:
#         print(numero)
#
#-----------------------------------------------------------------------
# WHILE

print("\t Escola Escolar")

nota1 = int(input("Digite o 1° nota: "))
while nota1 > 10:
    nota1 = int(input("Valor invalido \nDigite novamente: "))
nota2 = int(input("Digite o 2° nota: "))
while nota2 > 10:
    nota2 = int(input("Valor invalido \nDigite novamente: "))
nota3 = int(input("Digite o 3° nota: "))
while nota3 > 10:
    nota3 = int(input("Valor invalido \nDigite novamente: "))
nota4 = int(input("Digite o 4° nota: "))
while nota4 > 10:
    nota4 = int(input("Valor invalido \nDigite novamente: "))

media = (nota1+nota2+nota3+nota4) / 4

print("Média: {}".format(media))
