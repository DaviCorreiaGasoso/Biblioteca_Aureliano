from info_livro import Livro

biblioteca_Aureliano = []

def adicionar_livro (Livro):
    biblioteca_Aureliano.append(Livro)


def mostrar_acervo():
    print('Os livros Disponivéis são:\n')
    for livro in biblioteca_Aureliano:
        if livro.verificar_livro() == True:
            print (f'O título é: {livro.titulo}, O nome do autor(a) é: {livro.autor}, seu ano de publicação é: {livro.ano_publicado}\n')   

def emprestar_livro (titulo):
    for livro in biblioteca_Aureliano:
        if livro.titulo == titulo:
            livro.emprestar()
    

def devolver_livro (titulo):
    for livro in biblioteca_Aureliano:
        if livro.titulo == titulo:
            livro.disponibilizar_livro()
    

