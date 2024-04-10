from conectar import connect

def inserir(mydb, email, nome, senha, CPF):
        mycursor = mydb.cursor()

        sql = 'INSERT INTO usuario (email, nome, senha, CPF ) VALUES (%s, %s, %s, %s)'
        val = (email, nome, senha, CPF)

        mycursor.execute(sql, val)
        mydb.commit()

        print(mycursor.rowcount, "O usuário foi adicionado no nosso sistema, obrigado pela preferência!")

        mycursor.close()



def autenticar(mydb, email, senha):
        mycursor = mydb.cursor()
        sql = ('SELECT email, senha FROM usuario WHERE email = %s AND senha = %s')
        val = (email, senha)
        mycursor.execute(sql, val)
        resultado = mycursor.fetchall()

        for i, x in resultado:
                
            if email == i and senha == x:
                 print ( mycursor.rowcount,' Login aceito!')
                 return True
                 
        mycursor.close()
      
       