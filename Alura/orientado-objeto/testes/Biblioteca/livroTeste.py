class Livro:
    livros = []
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True
        Livro.livros.append(self)
        
    def __str__(self):
        return f'Titulo: {self.titulo} | Autor: {self.autor} | Ano de publicação: {self.ano_publicacao} | {self.disponivel}'
    
    def emprestar(self):
        self.disponivel = False
    
    @staticmethod
    def verificar_disponibilidade(ano_publi):
        livros_disponiveis = []
        for livro in Livro.livros:
            if livro.ano_publicacao == ano_publi and livro.disponivel:
                livros_disponiveis.append(livro)
        return livros_disponiveis
    
    
livro1 = Livro("Aprendendo Python", "John Doe", 2022)
livro2 = Livro("Data Science Fundamentals", "Jane Smith", 2022)
livro3 = Livro("Doctor Who", "Doctor", 1969)
livro2.emprestar()

#livros_disponiveis = Livro.verificar_disponibilidade(2022)

#for i in livros_disponiveis:
 #   print(i)


