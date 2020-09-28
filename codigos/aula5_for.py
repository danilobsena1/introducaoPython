print("\tUTILIZANDO FOR e range")

cidades = ["Salvador", "Camaçari", "Feira de Santana", "Candeias", 22]

for local in cidades:  # Para cada local(item) dentro de cidades, execute:
    print(local)    # MOSTRAR O NOME
print("---------------------------------------------------------")

print("#UTILIZANDO RANGE: ")

lista_de_numero = range(0, 5)
for item in lista_de_numero:
    print(item)
print("")
print("---------------------------------------------------------")

print("EXIBINDO VALORES DENTRO DO RANGE ENTRE 1 e 50 PULANDO  2 CASAS: ")
lista_de_numero = range(1, 50, 2)
for item in lista_de_numero:
    print(item)
print("")
print("---------------------------------------------------------")

cidades = ["Salvador", "Camaçari", "Feira de Santana", "Candeias", "Lauro de Freitas"]
for i in range(5):
    print(cidades[i])

print("---------------------------------------------------------")
frutas = ["Abacate", "Manga", "Caju", "Pera"]
for i in range(len(frutas)):    # Usado quando não se sabe a quantidade de itens dentro da lista.
    print(frutas[i])

print("---------------------------------------------------------")

frutas = ["Abacate", "Manga", "Caju", "Pera"]
for i in range(len(frutas)):
    print(frutas[i])
    frutas.append("OII: ") # Adicionando novos item a cada iteração.

print(frutas)

print("---------------------------------------------------------")

# IMPRIMINDO UM CARACTERE POR VEZ
palavra = "O palmeiras não tem mundial"
for i in palavra:
    print(i)

# ==========================================================

i = 0
for i in range(5):
    if i == 3:
        break
    print(i)


i = 0
for i in range(15):
    if i == 3:
        continue
    print(i)
