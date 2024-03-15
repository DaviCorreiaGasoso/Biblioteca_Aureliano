import biblioteca

print ('\nBem-vindo à Biblioteca Aureliano! ')
print('\nVocê pode fazer as seguintes ações:')
print('\n 1- Adicionar livro \n 2- Delvolver livro \n 3- Emprestar livro \n 4- Mostrar acervo \n 5- Sair do sistema')
acao = int(input('\nDigite o número da ação da sua escolha: '))
cont = 0

while cont < 1:
    if acao == 1:
        t = input('Digite o titulo do livro: ')
        a = input('Digite o(a) autor(a) do livro: ')
        ap = input('Digite o ano de publicação do livro: ')
        l = biblioteca.Livro(t,a,ap)
        biblioteca.adicionar_livro(l)
        print('\nO livro foi adicionado no nosso acervo, obrigado pela ajuda!')


    elif acao ==2:
        t = input('Digite o titulo do livro que você quer devolver: ')
        biblioteca.devolver_livro(t)
        print('\nO livro foi devolvido, obrigado por escolher nossa biblioteca!')
 
        
    elif acao ==3:
        t = input('Digite o titulo do livro que você quer pegar: ')
        biblioteca.emprestar_livro(t)
        print('\nO livro foi emprestado, obrigado por escolher nossa biblioteca!')

    elif acao ==4:
        print('Esse é o nosso acervo ')
        biblioteca.mostrar_acervo()

    elif acao ==5:
        cont = 2
        break

    else:
        print('Número de escolha inválido, digite novamente')

    print('\nVocê pode fazer as seguintes ações:')
    print('\n1- Adicionar livro \n 2- Delvolver livro \n 3- Emprestar livro \n 4- Mostrar acervo \n 5- Sair do sistema')
    acao = int(input('Digite o número da ação da sua escolha: '))
    

print('Você saiu do sistema, até a próxima!!')
        