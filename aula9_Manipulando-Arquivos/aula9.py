import shutil

# criando  o arquivo:
    # arquivo = open("aula9_teste.txt", "w")

# escrevendo no arquivo:
    # arquivo.write("Minha primeira escrita!")
    # arquivo.close() # fechando a abertura do arquivo

# Caso precise inserir novas informações no arquivo utilize o a:
    # arquivo = open("aula9_teste.txt", "a")
    # arquivo.write("\nSegunda linha!")
    # arquivo.close()

#Criando metodo
def escrever_arquivo(texto):
    arquivo = open("../codigos/teste.txt", "w")
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(texto):
    arquivo = open("../codigos/teste.txt", "a")
    arquivo.write(texto)
    arquivo.close()

# LENDO ARQUIVO
def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, "r")
    texto = arquivo.read()
    print(texto)

# COPIANDO ARQUIVO:
def copia_arquivo(nome_arquivo):
    # import shutil
# Copiando um arquivo para outro diretorio
    shutil.copy(nome_arquivo, "~/PycharmProjects/IntroducaoPython/codigos/notasAlunosteste.txt")

# MOVENDO ARQUIVO
def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, "~/PycharmProjects/IntroducaoPython/Pyhton-MYSQL/python-avancado")


if __name__ == '__main__':
    # COPIANDO ARQUIVO
    # copia_arquivo("aula9_teste.txt")

    #MOVENDO ARQUIVO
    move_arquivo("aula9_teste.txt")

    # Escrevendo arquivo:
    # escrever_arquivo("Primeira linha.\n")

    # Atualizando Arquivo:
    # atualizar_arquivo("Segunda linha.\n")

    # Lendo arquivo:
    # ler_arquivo("teste.txt")