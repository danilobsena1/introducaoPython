#TUPLAS

exemplo_tupla = (1, 2, 3, 4)

# Tuplas são imutaveis os valores dentro da lista não podem ser alterados:
#
# tupla_teste = (1, 2)
# print(tupla_teste)
# # NÃO É PERMITIDO A ALTERAÇÃO DO ITEM NA POSIÇÃO 0
# tupla_teste[0] = 3
# print(tupla_teste)

# VERIFICANDO A QUANTIDADE DE ITENS DENTRO DA TUPLA
#
# print(len(exemplo_tupla))

# CONVERTENDO LISTA PARA TUPLA
#
# lista_animal = ["Cachorro", "Gato", "Elefante"]
#
# tupla_animal = tuple(lista_animal)
# print(type(tupla_animal))
# print(tupla_animal)

# CONVERTENDO TUPLA PARA LISTA

# lista_numerica = list(exemplo_tupla)
# print(type(lista_numerica))
# print(lista_numerica)
# lista_numerica[1] = 48
# print(lista_numerica)

lista = [3, 5, 7, 10, 11]

resultado = [] # 3,5,7,11

for x in lista:

    if x % 2 == 1:

        resultado.append(x)

print(resultado)