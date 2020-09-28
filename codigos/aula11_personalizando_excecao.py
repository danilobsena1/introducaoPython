# CRIANDO CLASSES DE ERRO
class Error(Exception):  # Classe erro herda de Exception
    pass

class InputError(Error): # Classe InputError  herda de Error
    def __init__(self, message): # Construtor
        self.message = message

while True:
    try:
        x = int(input("Entre com uma nota de 0 a 10: "))
        print(x)
        if x > 10:
            raise InputError("Nota não pode ser maior que 10!")  #Forçando uma excessao
        elif x < 0:
            raise InputError("Nota não pode ser menor que 0!")
        break
    except ValueError:
        print("Valor invalido. Digite apenas números!")
    except InputError as ex:
        print(ex)
