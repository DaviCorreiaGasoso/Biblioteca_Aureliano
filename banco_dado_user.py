from conectar import connect

def inserir(mydb, email, nome, senha, cpf ):
        mycursor = mydb.cursor()

        sql = 'INSERT INTO livros (email, nome, senha, CPF ) VALUES (%s, %s, %s, %s)'
        val = (email, nome, senha, cpf)

        mycursor.execute(sql, val)
        mydb.commit()

        print(mycursor.rowcount, "o usuario foi adicionado no nosso sistema, obrigado pela ajuda!")

        mycursor.close()

