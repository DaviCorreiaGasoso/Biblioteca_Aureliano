class Livro:
    def __init__(self, titulo, autor, ano_publicado):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicado = ano_publicado
        self.status = True

    def emprestar(self):
        if self.status == True:
            self.status = False
        return self.status
        

    
    def disponibilizar_livro (self):
        if self.status == False:
            self.status = True
        return self.status
        
        
    def verificar_livro (self):
        return self.status

