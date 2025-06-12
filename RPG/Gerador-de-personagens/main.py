import random

print("Bem vindo ao gerador de personagens!\n obs: Nessa primeira versão você poderá gerar apenas aleatoriamente.")

racas = [
    "Aasimar", 
    "Anão", 
    "Draconato", 
    "Elfo",
    "Gnomo", 
    "Golias",
    "Humano", 
    "Orc",
    "Halfling",
    "Tiefling"
]

classes = [
    "Bárbaro",
    "Bardo",
    "Bruxo",
    "Clérigo",
    "Druida",
    "Feiticeiro",
    "Guerreiro",
    "Ladino",
    "Mago",
    "Monge",
    "Paladino",
    "Patrulheiro"
]

Atributos = [
    "Força",
    "Destreza",
    "Constituição",
    "Inteligência",
    "Sabedoria",
    "Carisma"
]

raca_escolhida = random.choice(racas)
classe_escolhida = random.choice(classes)

def gerar_atributo():
    return random.randint(8, 15)

forca = gerar_atributo()
destreza = gerar_atributo()
constituicao = gerar_atributo()
inteligencia = gerar_atributo()
sabedoria = gerar_atributo()
carisma = gerar_atributo()

print(
    f"FOR ({forca}) \n"
    f"DES ({destreza}) \n"
    f"CON ({constituicao}) \n"
    f"INT ({inteligencia}) \n"
    f"SAB ({sabedoria}) \n"
    f"CAR ({carisma}) \n"
)

