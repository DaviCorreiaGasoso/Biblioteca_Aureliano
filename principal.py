from conectar import connect
import banco_dados_livro
import banco_dado_usuario


def login():
    acesso = False  
     
    while acesso == False:
        
        login = str(input('Você tem uma conta? Responda com "sim" ou "não": '))

        if login.lower() == 'não':
            mydb = connect()

            print('\nBem-vindo(a) ao cadastro da Biblioteca Aureliano!\n')
            e = input('Digite seu email: ')
            n = input('Digite seu nome completo: ')
            s = input('Digite sua senha (não se esqueça da sua senha!!): ')
            CPF = input('Digite seu CPF: ')
            
            banco_dado_usuario.inserir(mydb, e, n.title(), s, CPF)
            print('\nAgora você está logado!\n')

            mydb.close()
            acesso = True
            return acesso

        
        
        elif login.lower() == 'sim':
            mydb = connect()

            print('Entre na sua conta!')
            e = input('Digite seu email: ')
            s = input('Digite sua senha: ')
            log = banco_dado_usuario.autenticar(mydb, e, s)

            mydb.close()
            if log == True:
                acesso = True
                return acesso

    else:
        print('Digite algo válido!')


def principal (autenticado):

    while True:
        print('\nVocê pode fazer as seguintes ações:')
        print('\n 1- Adicionar livro \n 2- Delvolver livro \n 3- Emprestar livro \n 4- Mostrar acervo \n 5- Excluir livro \n 6- Atualizar livro \n 7- Login \n 8- Sair do sistema ')
        acao = int(input('\nDigite o número da ação da sua escolha: '))

        if acao == 1:
            mydb = connect()

            t = input('Digite o titulo do livro: ')
            a = input('Digite o(a) autor(a) do livro: ')
            ap = input('Digite o ano de publicação do livro: ')
            d = "Disponivel"
            banco_dados_livro.inserir(mydb, t.title(), a.title(), ap, d)
            
            mydb.close()
            
        elif acao ==2:
            if autenticado == True:
                mydb = connect()
                t = input('Digite o titulo do livro que você quer devolver: ')
                banco_dados_livro.devolver_livro(t.title())
                print('\nO livro foi devolvido, obrigado por escolher nossa biblioteca!')
        
                mydb.close()
            
            else:
                print('Entre na sua conta para acessar essa ação!')

        elif acao ==3:
            if autenticado == True:
                mydb = connect()

                t = input('Digite o titulo do livro que você quer pegar: ')
                banco_dados_livro.emprestar_livros(t.title())
                
                mydb.close()
            
            else:
                print('Entre na sua conta para acessar essa ação!')

        elif acao ==4:
            mydb = connect()

            print('Esse é o nosso acervo: ')
            banco_dados_livro.mostrar_livros(mydb)

            mydb.close()

        elif acao ==5:
            if autenticado == True:
                mydb= connect()

                t = str(input('Digite o título do livro que você deseja excluir: '))
                banco_dados_livro.excluir_livros(mydb,t.title())

                mydb.close()
            
            else:
               print('Entre na sua conta para acessar essa ação!')
 

        elif acao ==6:
            if autenticado == True:
                mydb = connect()

                t = str(input('Digite o título do livro que você deseja atualizar: '))
                a = str(input('Digite o autor(a) do livro que você deseja atualizar: '))
                ap = str(input('Digite o ano de publicação do livro que você deseja atualizar: '))
                banco_dados_livro.atualizar_livro(mydb, t.title(), a.title(), ap)

                mydb.close()
            
            else:
               print('Entre na sua conta para acessar essa ação!')
    
        elif acao ==7:
            print('Para entrar em uma conta, sai do sistema para entrar na conta desejada')

        elif acao ==8:
            break

        else:
            print('Número de escolha inválido, digite novamente')   

    print('Você saiu do sistema, até a próxima!!')


print ('\nBem-vindo(a) à Biblioteca Aureliano! ')

atitude = str(input('\nVocê quer entrar na sua conta ou criar uma? Responda com "sim" ou "não": '))

if atitude.lower() == "não":
    condicao = False
    principal(condicao)

elif atitude.lower() == "sim":
    login()
    condicao = True
    principal(condicao)
    

else:
    print('Digite algo válido!')