# a = int(input("Primeiro valor: "))
# b = int(input("Segundo valor: "))
# c = int(input("Terceiro valor: "))
#
# if a > b and a > c:
#     print("O maior número é {}".format(a))
# elif b > a and b > c:
#     print("O maior numero é {}".format(b))
# else:
#     print("O maior número é {}".format(c))
#
# print("Programa encerrado")
#
# print("--------------------------------------------------")
#
# print("VERIFICANDO SE O NÚMERO É PAR")
#
# numero = int(input("Digite o número: "))
# if numero % 2 == 0:
#     print("Número {}".format(numero) + " é par")
# else:
#     print("Número {}".format(numero) + " é impar")

# print("--------------------------------------------------")
#
# print("VERIFICANDO SE FOI DIGITADO UM NUMERO PAR")
#
# num1 = int(input("Digite o 1° valor: "))
# num2 = int(input("Digite o 2° valor: "))
# resto_num1 = num1 % 2
# resto_num2 = num2 % 2
#
# if resto_num1 == 0 and resto_num2 == 0:
#     print("Foram digitados dois número pares")
#     if resto_num1 == 0:
#         print("Número par digitado foi: {}".format(num1))
#     if resto_num2 == 0:
#         print("Número par digitado foi: {}".format(num2))
# elif resto_num1 == 0 or resto_num2 == 0:
#     print("Foi digitado pelo menos um número par")
#     if resto_num1 == 0:
#         print("Número par digitado foi: {}".format(num1))
#     if resto_num2 == 0:
#         print("Número par digitado foi: {}".format(num2))
# else:
#     print("Nenhum número par foi digitado")
#
# print("--------------------------------------------------")
#
# print("MEDIA DE UM ALUNO")
#
# print("\t Escola Escolar")
# nota1 = int(input("Digite o 1° nota: "))
# nota2 = int(input("Digite o 2° nota: "))
# nota3 = int(input("Digite o 3° nota: "))
# nota4 = int(input("Digite o 4° nota: "))
#
# media = (nota1+nota2+nota3+nota4) / 4
#
# if nota1 <= 10 and nota2 <= 10 and nota3 <= 10 and nota4 <= 10:
#     print("Média: {}".format(media))
# else:
#     print("Foi inserido alguma nota com valor incorreto")

print("--------------------------------------------------")

print("VALIDANDO OS VALORES LOGO NO INICIO:")

print("\t Escola Escolar")

nota1 = int(input("Digite o 1° nota: "))
if nota1 > 10:
    nota1 = int(input("Valor invalido \nDigite novamente: "))
nota2 = int(input("Digite o 2° nota: "))
if nota2 > 10:
    nota2 = int(input("Valor invalido \nDigite novamente: "))
nota3 = int(input("Digite o 3° nota: "))
if nota3 > 10:
    nota3 = int(input("Valor invalido \nDigite novamente: "))
nota4 = int(input("Digite o 4° nota: "))
if nota4 > 10:
    nota4 = int(input("Valor invalido \nDigite novamente: "))

media = (nota1+nota2+nota3+nota4) / 4

print("Média: {}".format(media))

print("================================================================")