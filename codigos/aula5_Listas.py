#LISTAS

# Listas são mutaveis os valores dentro da lista podem ser alterados:
lista_teste = [1, 2]
print(lista_teste)
lista_teste[0] = 3
print(lista_teste)

lista = [1, 3, 5, 7]

lista_animal = ["Cachorro", "Gato", "Elefante"]

lista_animal1 = ["Cachorro", "Gato", "Elefante", "Lobo", "Arara"]

lista_repteis = ["Cobra", "jacaré", "crocodilo", "camaleão", "iguana", "lagarto"]

# print(type(lista_animal))
# print(lista_animal[1])
# print(lista_repteis)

# PERCORRENDO A LISTA ATRAVÉS DE UM LAÇO DE REPETIÇÃO

    # for x in lista_animal:
    # print(x)

# -----------------------------------------------------
# SOMANDO OS VALORES DA LISTA

    # soma = 0
    # for x in lista:
    #     print(x)
    #     soma = soma + x
    # print("Soma: {}".format(soma))

# __OUTRA FORMA DE EXIBIR O TOTAL DA LISTA

    # print(sum(lista))
    # print("Soma = {}".format(sum(lista)))

# -----------------------------------------------------

# BUSCANDO O MAIOR VALOR DA LISTA
    # print(max(lista))
    # print(max(lista_animal))
    # Imprime gato pq começa com a letra g que é a maior do alfabeto presente dentro dessa lista.

# BUSCANDO O MENOR VALOR DA LISTA
    # print(min(lista_animal))
    # imprime cachorro pq a palavra começa com a letra c

# ----------------------------------------------------

# MULTIPLICANDO(REPETINDO) VALORES DENTRO DA LISTA

# lista_numero = [1] * 3
# print(lista_numero)

# -----------------------------------------------------

# VERIFICANDO A EXISTÊNCIA DE VALORES DENTRO DA LISTA

# if "Vaca" in lista_animal:
#     print("Existe uma vaca na lista")
# else:
#     print("Não existe uma vaca na lista")

# ADICIONANDO VALORES DENTRO DA LISTA

# print("Lista de Animais: {}\n".format(lista_animal))
# if "Vaca" in lista_animal:
#     print("Existe uma vaca na lista")
# else:
#     print("Não existe uma vaca na lista. \nO animal será adicionando")
#     lista_animal.append("Vaca")
#     print("Atualizando dados...")
#     print("Lista de Animais: {}\n".format(lista_animal))

# REMOVENDO VALORES DENTRO DA LISTA

# pop() vai remover o ultimo item da lista.
# lista_repteis.pop()
# print(lista_repteis)

# pop(1) Vai remover o item na posição 1
# lista_repteis.pop(1)
# print(lista_repteis)

# Para remover um item que você já conhce utiliza-se o remove
# lista_repteis.remove("crocodilo")
# print(lista_repteis)

# -----------------------------------------------------
# ORDENANDO OS ITENS DA LISTA
#
# lista.sort()
# lista_animal1.sort()
# lista_repteis.sort()
# print(lista)
# print(lista_animal1)
# print(lista_repteis)

# REVERTENDO(ordenando de trás para frente) OS ITENS DA LISTA
#
# lista.reverse()
# lista_animal1.reverse()
# print(lista)
# print(lista_animal1)

# -----------------------------------------------------
# VERIFICANDO A QUANTIDADE DE ITENS DENTRO DA LISTA

print(len(lista_repteis))

