dicionario = {"a":"amarelo", "b":"branco","v":"verde"}
print (dicionario)

print(dicionario.values())

print("-------------------------------------------")
print("IMPRIMINDO ITEM DO DICIONARIO")
print(dicionario["a"])

print("-------------------------------------------")
print("UTILIZANDO O FOR NO DICIONARIO")

for chave in dicionario:
    print(chave+":"+dicionario[chave])
    # OU print(chave,":",dicionario[chave])

print("-------------------------------------------")
for i in dicionario.values():
    print(i)