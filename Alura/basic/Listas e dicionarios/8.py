# 8) Para uma seleção de produtos alimentícios, precisamos separar o conjunto de IDs dados por números inteiros 
# sabendo que os produtos com ID par são doces e os com ID ímpar são amargos. Monte um código que colete 10 IDs. 
# Depois, calcule e mostre a quantidade de produtos doces e amargos.

produtosID = []
produtosAmargo = []
produtosDoce = []

for i in range(0, 10):
    produto = int(input('Digite o ID do produto: '))
    produtosID.append(produto)

for i in range(0, 10):
    verifica = produtosID[i] % 2
    if verifica != 0:
        produtosAmargo.append(produtosID[i])  
    else:
        produtosDoce.append(produtosID[i])    

print("Produtos Amargos:", produtosAmargo)
print("Produtos Doces:", produtosDoce)
print("Quantidade de produtos amargos:", len(produtosAmargo))
print("Quantidade de produtos doces:", len(produtosDoce))