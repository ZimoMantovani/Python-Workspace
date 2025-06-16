import random

from faker import Faker

print("Bem vindo ao gerador de personagens!\n obs: Nessa primeira versão você poderá gerar apenas aleatoriamente.")

fake = Faker()
nomes_fantasia = [fake.unique.first_name() for _ in range(20)]
nome = random.choice(nomes_fantasia)  # escolhe um nome aleatório da lista
print(nome)


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

Alinhamento = [
    "Leal e Bom",
    "Neutro e Bom",
    "Caótico e Bom",
    "Leal e Neutro",
    "Neutro",
    "Caótico e Neutro",
    "Leal e Mau",
    "Neutro e Mau",
    "Caótico e Mau"
]

Historico = [
    "Acólito",
    "Artífice",
    "Criminoso",
    "Erudito",
    "Folk Hero",
    "Nobre",
    "Soldado",
    "Sage",
    "Hermit",
    "Outlander"
]


raca_escolhida = random.choice(racas)
classe_escolhida = random.choice(classes)
historico_escolhido = random.choice(Historico)
alinhamento_escolhido = random.choice(Alinhamento)

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

#Combate 


