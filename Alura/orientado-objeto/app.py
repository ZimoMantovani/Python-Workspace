from modelos.restaurante import Restaurante

restaurante_praca = Restaurante("praça", "Gourmet")
# restaurante_mexicano = Restaurante("Mexican Food", "Mexicana")
# restaurante_japones = Restaurante("Japa", "Japonesa")

restaurante_praca.receber_avaliacao("Zimo",10)
restaurante_praca.receber_avaliacao("Lais",8)
restaurante_praca.receber_avaliacao("Jooj",5)

def main():
    Restaurante.listar_restaurantes()

if __name__ == "__main__":
    main()