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

def emprestar_livros(mydb, titulo):
       mycursor = mydb.cursor()

       sql = 'SELECT status_livro FROM livros WHERE titulo = %s'
       val = (titulo)
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
              sql_update = 'UPDATE livros SET status_livro = %s WHERE  = %s'
              val_update = ('Emprestado', titulo)
              mycursor.execute(sql_update, val_update)
       mydb.commit()
       print(f"O livro {titulo} foi emprestado com sucesso!")

       mycursor.close()

def excluir_livros(mydb,titulo):
       mycursor = mydb.cursor()

       sql= 'DELETE FROM livros (titulo) VALUES (%s)'
       val= (titulo)

       mycursor.execute(sql,val)
       mydb.commit()
       print(mycursor.rowcount, 'O livro foi excluído do nosso acervo!')
       
       mycursor.close()
       
def devolver_livro(mydb, titulo):
       mycursor = mydb.cursor()

       sql = 'SELECT status_livro FROM livros WHERE titulo = %s'
       val = (titulo)
       mycursor.execute(sql, val)
       livro_status = mycursor.fetchone()

       if livro_status is None:
              print("Livro não encontrado.")
              mycursor.close()
              return
       elif livro_status[0] == 'Disponivel':
              print("O livro já foi devolvido.")
              mycursor.close()
              return
       else:
              sql_update = 'UPDATE livros SET status_livro = %s WHERE titulo = %s'
              val_update = ('Disponível', titulo)
              mycursor.execute(sql_update, val_update)
       mydb.commit()
       print(f"O livro {titulo} foi devolvido com sucesso!")

       mycursor.close()
    
def atualizar_livro(mydb, titulo, autor, ano_publicado):
       mycursor = mydb.cursor()

       sql_update= 'UPDATE livros SET titulo = %s, autor = %s, ano_publicado = %s, where titulo = %s'
       val_update= (titulo, autor, ano_publicado, titulo)
       mycursor.execute(sql_update, val_update)
       mydb.comit()
       print(mycursor.rowcount, "As informações do livro foram atualizadas com sucesso!")

       mycursor.close()


       