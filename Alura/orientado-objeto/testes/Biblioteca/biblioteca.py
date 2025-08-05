from livroTeste import Livro

livro1 = Livro("Ola mundo", "Zimo", 2022)

#livro1.emprestar()

livros_disponiveis = Livro.verificar_disponibilidade(2022)

for livro in livros_disponiveis:
    print(livro)

#print(livro1)