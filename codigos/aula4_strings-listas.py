print("\t UTILIZANDO LISTAS: ")

lista_nomes = ["Joao", "Maria", "Guilherme", "Roberto", 10, 10.3, False]

print(lista_nomes[0])
print(lista_nomes)
print(lista_nomes[0:2])

print("-------------------------------------------------------------------")
print("Imprimindo o ultimo item da lista: ")
print(lista_nomes[-1])

print("-------------------------------------------------------------------")
print("Invertendo a ordem dos itens contido na lista: ")
print(lista_nomes[::-1])

print("____________________________________________________________________")
print("Adicionando mais nomes na lista: ")
lista_nomes.append("Fabiola")
lista_nomes.append("Rafaela")
lista_nomes.append("Fabiola")
print(lista_nomes)
print("____________________________________________________________________")
print("Verificando a quantidade de  itens iguais em uma lista: Fabiola ")
contador = lista_nomes.count("Fabiola")
print(contador, "itens")

print("-------------------------------------------------------------------")
print("Verificando a quantidade de  itens totais em uma lista: ")
print(len(lista_nomes))

print("-------------------------------------------------------------------")
print("Adicionando item em determinado indice da lista: ")
lista_nomes.insert(1, "Guanabara")
print(lista_nomes)

print("____________________________________________________________________")
print("modificando item em determinado indice da lista: ") # O item que continha o valor Guanabara será substituido por Clodoaldo
lista_nomes[1] = "Clodoaldo"
print(lista_nomes)

print("____________________________________________________________________")
print("Removendo nome da lista: ")
lista_nomes.remove("Guilherme")
print(lista_nomes)
print("-------------------------------------------------------------------")

print("REMOVENDO ELEMENTOS")
teste = ["a", "b", "c", "d"]
del teste[1:4]
print(teste)

print("-------------------------------------------------------------------")
print("Limpando os itens da lista: ")
lista_nomes.clear()
print(lista_nomes)

print("-------------------------------------------------------------------")

print("####################################################################")
print("Strings: \n")

frase = "Oi, tudo bem?"
print(frase)
print(frase[0:5])
print(frase[3:7])

print("-------------------------------------------------------------------")
print("Verificando a quantidade de  itens totais em uma String: ")
print(len(frase))

print("-------------------------------------------------------------------")
print("Imprima de 0 até 5 pulando de dois em dois caractere: ")
print(frase[0:7:2])

print("-------------------------------------------------------------------")
print("Invertendo a ordem dos itens contido na string: ")
print(frase[::-1])

print("-------------------------------------------------------------------")
print("Passando tudo para minusculo: ")
print(frase.lower()) # As letras passam para miniscula somente enquanto o comando é executado.
print(frase)
print("-------------------------------------------------------------------")

print("ORDENANDO A LISTA EM ORDEM DECRESCENTE")
listaNumeros = [6, 8, 7, 41, 1, 0, 2, 65, 10]
listaNumeros.sort(reverse=True)
print(listaNumeros)