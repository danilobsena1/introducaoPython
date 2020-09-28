class Error(Exception):  # Classe erro herda de Exception
    pass

class InputError(Error):  # Classe InputError  herda de Error
    def __init__(self, message):  # Construtor
        self.message = message

while True:
    total = 0
    media = 0
    try:

        quantidade = int(input("Entre com a quantidade de notas: "))
        if quantidade <= 0:
            raise InputError("Nota não pode ser menor que 0!")

        for i in range(0, quantidade):
            nota = float(input("Digite a nota: "))
            total += nota
        media = total / int(quantidade)

        print("Média: {}".format(media))
        break
    except ValueError:
        print("Valor invalido. Digite apenas números!")
    except InputError as ex:
        print(ex)