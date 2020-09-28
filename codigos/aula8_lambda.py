# def contador_letras(lista_palavras):
#     contador = []
#     for x in lista_palavras:
#         quantidade = len(x)
#         contador.append(quantidade)
#     return contador
#
# if __name__ == '__main__':
#     lista = ["peixe","tubarão"]
#     print(contador_letras(lista))

print("Utilizando Lambda")

contador_letras = lambda lista: [len(x) for x in lista]

lista_animais_marinhos = ["sardinha", "lula", "caranguejo"]
print(contador_letras(lista_animais_marinhos))

print("Criando uma Calculadora")
# Utilizando dicionario:
calculadora = {
    "soma": lambda a, b: a + b,
    "subtracao": lambda a, b: a - b,
    "multiplicacao": lambda a, b: a * b,
    "Divisao": lambda a, b: a /b,
}
soma = calculadora["soma"]
subtracao = calculadora["subtracao"]
multiplicacao = calculadora["multiplicacao"]
divisao = calculadora["Divisao"]

print(soma(1,3))
print(subtracao(3, 4))
print(multiplicacao(5, 6))
print(int(divisao(30, 5)))