#4) Colete novamente 5 inteiros e imprima a lista em ordem inversa à enviada.

lista = []
for i in range(5):
    numero = int(input('Digite um número inteiro: '))
    lista.append(numero)

for i in reversed(lista):
    print(i)
