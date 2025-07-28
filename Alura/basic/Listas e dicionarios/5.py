# 5) Faça um programa que, ao inserir um número qualquer, cria uma lista contendo todos os números primos entre 1 e o número digitado.

lista = []
num = int(input("Digite um número inteiro: "))

for i in range(2, num + 1):
    lista.append(i)

for numTeste in lista.copy():
    for i in range(2, numTeste):
        if numTeste % i == 0:
            lista.remove(numTeste)
            break
            
print(lista)
