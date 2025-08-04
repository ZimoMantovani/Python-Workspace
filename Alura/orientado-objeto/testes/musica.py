class Musica:
    musicas = []
    def __init__(self,nome,artista,duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao 
        Musica.musicas.append(self)
        
    def mostra_musica():
        for muscas in Musica.musicas:
            print(f'{muscas.nome} | {muscas.artista} | {muscas.duracao}')



musica1 = Musica('Bohemian Rhapsody','Queen',355)
musica2 = Musica('Imagine','John Lennon',183)
musica3 = Musica('Shape of You','Ed Sheeran',234)


Musica.mostra_musica()