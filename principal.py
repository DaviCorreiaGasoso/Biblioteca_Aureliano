from conectar import connect
import banco_dados

print ('\nBem-vindo à Biblioteca Aureliano! ')
print('\nVocê pode fazer as seguintes ações:')

while True:
    print('\nVocê pode fazer as seguintes ações:')
    print('\n 1- Adicionar livro \n 2- Delvolver livro \n 3- Emprestar livro \n 4- Mostrar acervo \n 5- Excluir livro \n 6- Atualizar livro \n 7- Sair do sistema ')
    acao = int(input('\nDigite o número da ação da sua escolha: '))

    if acao == 1:
        mydb = connect()

        t = input('Digite o titulo do livro: ')
        a = input('Digite o(a) autor(a) do livro: ')
        ap = input('Digite o ano de publicação do livro: ')
        d = "Disponivel"
        banco_dados.inserir(mydb, t, a, ap, d)
        
        mydb.close()
        
    elif acao ==2:
        t = input('Digite o titulo do livro que você quer devolver: ')
        biblioteca.devolver_livro(t)
        print('\nO livro foi devolvido, obrigado por escolher nossa biblioteca!')
 
        
    elif acao ==3:
        mydb = connect()

        t = input('Digite o titulo do livro que você quer pegar: ')
        banco_dados.emprestar_livros(t)
        
        mydb.close()

    elif acao ==4:
        mydb = connect()

        print('Esse é o nosso acervo: ')
        banco_dados.mostrar_livros(mydb)

        mydb.close()

    elif acao ==5:
        mydb= connect()

        t=  str(input('Digite o título do livro que você deseja excluir: '))
        banco_dados.excluir_livros(mydb,t)
        mydb.close()

    else:
        print('Número de escolha inválido, digite novamente')

    

print('Você saiu do sistema, até a próxima!!')
        