from conectar import connect
import banco_dados_livro

print ('\nBem-vindo à Biblioteca Aureliano! ')


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
        banco_dados_livro.inserir(mydb, t, a, ap, d)
        
        mydb.close()
        
    elif acao ==2:
        mydb = connect()
        t = input('Digite o titulo do livro que você quer devolver: ')
        banco_dados_livro.devolver_livro(t)
        print('\nO livro foi devolvido, obrigado por escolher nossa biblioteca!')
 
        mydb.close()

    elif acao ==3:
        mydb = connect()

        t = input('Digite o titulo do livro que você quer pegar: ')
        banco_dados_livro.emprestar_livros(t)
        
        mydb.close()

    elif acao ==4:
        mydb = connect()

        print('Esse é o nosso acervo: ')
        banco_dados_livro.mostrar_livros(mydb)

        mydb.close()

    elif acao ==5:
        mydb= connect()

        t = str(input('Digite o título do livro que você deseja excluir: '))
        banco_dados_livro.excluir_livros(mydb,t)
        mydb.close()

    elif acao ==6:
        mydb = connect()

        t = str(input('Digite o título do livro que você deseja atualizar: '))
        a = str(input('Digite o autor(a) do livro que você deseja atualizar: '))
        ap = str(input('Digite o ano de publicação do livro que você deseja atualizar: '))
        banco_dados_livro.atualizar_livro(mydb, t, a, ap)

        mydb.close()
  
    elif acao ==7:
        break

    else:
        print('Número de escolha inválido, digite novamente')   

print('Você saiu do sistema, até a próxima!!')
        