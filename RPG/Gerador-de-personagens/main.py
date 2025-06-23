import random

from faker import Faker

print("Bem vindo ao gerador de personagens!\n obs: Nessa primeira versão você poderá gerar apenas aleatoriamente.")

fake = Faker()
nomes_fantasia = [fake.unique.first_name() for _ in range(20)]
nome = random.choice(nomes_fantasia)  # escolhe um nome aleatório da lista



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

atributos = [
    "Força",
    "Destreza",
    "Constituição",
    "Inteligência",
    "Sabedoria",
    "Carisma"
]

alinhamento = [
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

antecedente = [
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

pericias = [
    "Acrobacia",
    "Arcanismo",
    "Atletismo",
    "Atuação",
    "Enganação",
    "Furtividade",
    "História",
    "Intimidação",
    "Intuição",
    "Investigação",
    "Lidar com Animais",
    "Medicina",
    "Natureza",
    "Percepção",
    "Persuasão",
    "Prestidigitação",
    "Religião",
    "Sobrevivência"
]

equipamento_inicial = [
    "Espada curta",
    "Adaga",
    "Arco curto",
    "Machado de batalha",
    "Escudo",
    "Armadura de couro",
    "Armadura de malha",
    "Poção de cura",
    "Kit de explorador",
    "Kit de ladrão",
    "Livro de magias",
    "Instrumento musical",
    "Símbolo sagrado",
    "Pacote de aventureiro",
    "Rações de viagem",
    "Tocha",
    "Corda",
    "Mapa antigo",
    "Moeda de ouro",
    "Anel misterioso"
]


def gerar_atributo(): # Função para gerar um valor de atributo aleatório de 8 à 15.
    return random.randint(8, 15) 

def gerar_pericia(): # Escolhe 4 pericias da lista para se tornar proficiente (sample para não repetir)
    return random.sample(pericias, 4)

def gerar_equipamento():# Escolhe 6 equipamentos da lista 
    return random.sample(equipamento_inicial,6)

periciasEscolhidas = gerar_pericia()
equipamentoEscolhido = gerar_equipamento()

#Escolhe randomicamente o basico
raca_escolhida = random.choice(racas)
classe_escolhida = random.choice(classes)
antecedente_escolhido = random.choice(antecedente)
alinhamento_escolhido = random.choice(alinhamento)

#Gera randomicamente cada atributo
forca = gerar_atributo()
destreza = gerar_atributo()
constituicao = gerar_atributo()
inteligencia = gerar_atributo()
sabedoria = gerar_atributo()
carisma = gerar_atributo()

#Cria modificadores dos atributos
#Vou fazer depois



print(
    "📜 Basico do personagem \n"
    f"Nome: {nome}  \n"
    f"Raça: {raca_escolhida} \n"
    f"Classe: {classe_escolhida} \n"
    f"Alinhamento: {alinhamento_escolhido} \n"
    f"Antecedente: {antecedente_escolhido} \n\n"
    
    "🛡️ Atributos \n"
    f"FOR ({forca}) \n"
    f"DES ({destreza}) \n"
    f"CON ({constituicao}) \n"
    f"INT ({inteligencia}) \n"
    f"SAB ({sabedoria}) \n"
    f"CAR ({carisma}) \n"
    
    "Bônus de Proficiência: +2 \n\n"
    
    "💥 Perícias (proficiente em:) \n"
    f"Escolhidas: {periciasEscolhidas} \n\n"
    
    "🗡️ Equipamento Inicial \n"
    f"{equipamentoEscolhido}"
    
    f"❤️ Pontos de Vida: {10 + constituicao}"
)

#Combate 


