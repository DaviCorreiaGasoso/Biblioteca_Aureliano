from conectar import connect

def inserir(mydb, email, nome, senha, cpf ):
        mycursor = mydb.cursor()

        sql = 'INSERT INTO livros (email, nome, senha, CPF ) VALUES (%s, %s, %s, %s)'
        val = (email, nome, senha, cpf)

        mycursor.execute(sql, val)
        mydb.commit()

        print(mycursor.rowcount, "o usuario foi adicionado no nosso sistema, obrigado pela ajuda!")

        mycursor.close()



def autenticar(mydb, email, senha):
        mycursor = mydb.cursor()
        mycursor.execute('SELECT * FROM user WHERE email = %s AND senha = %s' , (email,senha))
        resultado = mycursor.fetchall()
        if autenticar:
              print('Login encontrado.')
        else:
              print ('Login inválido')
        
        mycursor.close()
