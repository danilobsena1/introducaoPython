# Dado o trecho de código abaixo, qual será o valor armazenado na variável “resultado”?

def minha_funcao(numero):
    if numero % 2 == 0:
        return '{} é par'.format(numero)
    else:
        return '{} é ímpar'.format(numero)

    return "zero é neutro"


resultado = minha_funcao(0)

print(resultado)