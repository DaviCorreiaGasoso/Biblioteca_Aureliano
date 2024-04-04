from conectar import connect


def inserir(mydb, titulo, autor, ano_publicado, status_livro):
        mycursor = mydb.cursor()

        sql = 'INSERT INTO livros (titulo, autor, ano_publicado, status_livro) VALUES (%s, %s, %s, %s)'
        val = (titulo, autor, ano_publicado, status_livro)

        mycursor.execute(sql, val)
        mydb.commit()

        print(mycursor.rowcount, "O livro foi adicionado no nosso acervo, obrigado pela ajuda!")

        mycursor.close()
    
def mostrar_livros(mydb):
        mycursor = mydb.cursor()

        mycursor.execute('SELECT * FROM livros')
        resultado = mycursor.fetchall()
        
        for i in resultado:
            print(i)
        
        mycursor.close()

    




