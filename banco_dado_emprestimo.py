from conectar import connect

def emprestar (mydb, id_emprestimos, id_usuario, id_livro, data_emprestimos, data_devolucao):
        mycursor = mydb.cursor()

        sql = 'INSERT INTO usuario (id_emprestimos, id_usuario, id_livro, data_emprestimos, data_devolucao ) VALUES (%s, %s, %s, %s)'
        val = (id_emprestimos, id_usuario, id_livro, data_emprestimos, data_devolucao)

        print(mycursor.rowcount, "Os dados dos seu emprestimo sâo: ")
  
        mycursor.close()