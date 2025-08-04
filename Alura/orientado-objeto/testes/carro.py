class Carro:
    carros = []
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        Carro.carros.append(self)
        pass
    
    def mostra_carro():
        for i in Carro.carros:
            print(f'{i.modelo} | {i.cor} | {i.ano}')
    
    
carro1 = Carro(modelo="Onix", cor="Prata", ano=2023)

carro2 = Carro(modelo="Renegade", cor="Cinza Chumbo", ano=2024)

carro3 = Carro(modelo="Strada", cor="Branco", ano=2025)

carro4 = Carro(modelo="Polo", cor="Preto", ano=2023)

carro5 = Carro(modelo="HB20", cor="Vermelho Metálico", ano=2022)

carro6 = Carro(modelo="Mobi", cor="Branco", ano=2024)

Carro.mostra_carro()