def escrever_arquivo(texto):
    arquivo = open("notas.txt", "w")
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, "a")
    arquivo.write(texto)
    arquivo.close()

def ler_arqivo(nome_arquivo):
    arquivo = open(nome_arquivo, "r")
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, "r")
    aluno_nota = arquivo.read()
    # print(aluno_nota)
    aluno_nota = aluno_nota.split("\n") # Toda vez que tiver uma quebra de linha o valor será adicionado em uma lista.
    # print(aluno_nota)
    lista_media =[]
    for i in aluno_nota:
        lista_notas = i.split(",") # Toda vez que tiver uma virgula o valor será adicionado em uma lista.
        aluno = lista_notas[0]
        lista_notas.pop(0) # Irá remover o 1° item da lista, nesse caso o nome.
        print(aluno)
        print(lista_notas)
        # Convertendo os itens da lista para inteiro e fazendo o calculo com o sum.
        media = lambda notas:sum([int(i) for i in notas]) / 4
        print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})
    return lista_media


if __name__ == '__main__':
     lista_media= media_notas("notas.txt")
     print(lista_media)
    # aluno = "Maria, 10, 7, 8, 6\n"
    # atualizar_arquivo("notas.txt", aluno)
    # ler_arqivo("notas.txt")