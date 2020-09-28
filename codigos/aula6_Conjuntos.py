print("CONJUNTOS")

# CONJUNTO NÃO ACEITA ITENS DUPLICADOS
conjunto_teste = {1, 1, 3, 4, 4, 6, 6}
print(conjunto_teste)
# SAIDA = {1, 3, 4, 6}

print("---------------------------------------------")
print("UNINDO ITENS DOS CONJUNTOS")
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}

conjunto_uniao = conjunto1.union(conjunto2)
print("Resultado da união: {}".format(conjunto_uniao))

# SAIDA = Resultado da uniao: {1, 2, 3, 4, 5, 6, 7, 8}

print("--------------------         ----------------------")
# EXIBINDO OS ITENS REPETIDOS(intersecção) DENTRO DOS CONJUNTOS

conjunto_interseccao = conjunto1.intersection(conjunto2)
print("Resultado da intersecção: {}".format(conjunto_interseccao))

# SAIDA = Resultado da intersecção: {5}

print("--------------------         ----------------------")
# EXIBINDO A DIFERENÇA ENTRE OS CONJUNTOS

print("Conjunto1: {}".format(conjunto1))
print("Conjunto2: {}".format(conjunto2))


# conjunto1 = {1, 2, 3, 4, 5}
# conjunto2 = {5, 6, 7, 8}

conjunto_diferenca1 = conjunto1.difference(conjunto2)
print("Diferença entre 1 e 2: {}".format(conjunto_diferenca1))
# SAIDA = Diferença entre 1 e 2: {1, 2, 3, 4} O conjunto1 possui de diferente os itens: 1 2 3 4

conjunto_diferenca2 = conjunto2.difference(conjunto1)
print("Diferença entre 2 e 1: {}".format(conjunto_diferenca2))
# SAIDA = Diferença entre 2 e 1: {8, 6, 7} O conjunto2 possui de diferente os itens: 8 6 7

print("------------------------------------------------------")

# DIFERENÇA SIMETRICA DOS CONJUNTOS
# Serão exibidos apenas os valores que não se repetem nos conjuntos.

nomes = {"Pedro", "Tiago", "João", "Barquinho"}
nomes2 = {"Peu", "Barquinho", "Trigo", "Joao"}

conjunto_simetrico = nomes.symmetric_difference(nomes2)
print("Diferença simetrica: {}".format(conjunto_simetrico))
# SAIDA = Diferença simetrica: {'João', 'Tiago', 'Pedro', 'Trigo', 'Peu', 'Joao'}

print("------------------------------------------------------")

print(" \t CONJUNTO SUBSET ")
# Verifica se um conjunto é subconjunto do outro

conjuntoA = {1, 2, 3}
conjuntoB = {1, 2, 3, 4, 5}

conjunto_subset = conjuntoA.issubset(conjuntoB)
print("A è suconjunto de B: {}".format(conjunto_subset))
# SAIDA = A è suconjunto de B: True  .Pois conjuntoA possui os mesmos elementos do conjuntoB

conjunto_subset = conjuntoB.issubset(conjuntoA)
print("B è suconjunto de A: {}".format(conjunto_subset))
# SAIDA = B è suconjunto de A: False .Pois conjuntoA não possui todos os elementos do conjuntoB

# ------------------------------------------------------------
print("------------------------------------------------------")

print("\t CONJUNTO SUPERSET")
#  um conjunto é superset quando ele tem outro(s) subconjunto(s)

conjSuperSet = conjuntoB.issuperset(conjuntoA)
print("B é um superconjunto de A: {}".format(conjSuperSet))

# SAIDA = B é um superconjunto de A True

conjSuperSet = conjuntoA.issuperset(conjuntoB)
print("A é um superconjunto de B: {}".format(conjSuperSet))

# SAIDA = A é um superconjunto de B : False

# ------------------------------------------------------------
print("------------------------------------------------------")

# CONVERTENDO LISTA PARA CONJUNTO

lista_peixes = ["Tubarão", "Tubarão", "Sardinha", "Rubalo", "Atum"]
print(lista_peixes)
conjunto_peixes = set(lista_peixes)
print(conjunto_peixes)

# CONVERTENDO NOVAMENTE PARA LISTA
lista_peixes = list(conjunto_peixes)
print(lista_peixes)