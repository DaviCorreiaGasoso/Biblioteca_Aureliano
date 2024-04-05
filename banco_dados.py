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

def emprestar_livros(mydb, titulo, status_livro):
       mycursor = mydb.cursor()
       sql = 'SELECT status_livro FROM livros WHERE id = %s'
       val = (status_livro)
       mycursor.execute(sql, val)
       livro_status = mycursor.fetchone()

       if livro_status is None:
              print("Livro não encontrado.")
              mycursor.close()
              return
       elif livro_status[0] == 'Emprestado':
              print("Desculpe, o livro já está emprestado.")
              mycursor.close()
              return
       else:
              sql_update = 'UPDATE livros SET status_livro = %s WHERE id = %s'
              val_update = ('Emprestado', status_livro)
              mycursor.execute(sql_update, val_update)
       mydb.commit()
       print("Livro emprestado com sucesso!")
       mycursor.close()

def excluir_livros(mydb,titulo):
       mycursor = mydb.cursor()

       sql= 'DELETE FROM livros (titulo) VALUES (%s)'
       val= (titulo)

       mycursor.execute(sql,val)
       mydb.commit()
       print(mycursor.rowcount, 'O livro foi excluído do nosso acervo!')
       
       mycursor.close()
       

    




