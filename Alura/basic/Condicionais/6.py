valor1 = int(input('Digite o valor 1: '))
valor2 = int(input('Digite o valor 2: '))
valor3 = int(input('Digite o valor 3: '))

if valor1 >= valor2 and valor1 >= valor3:
    if valor2 >= valor3:
        print(valor1, valor2, valor3)
    else:
        print(valor1, valor3, valor2)
elif valor2 >= valor1 and valor2 >= valor3:
    if valor1 >= valor3:
        print(valor2, valor1, valor3)
    else:
        print(valor2, valor3, valor1)
else:
    if valor1 >= valor2:
        print(valor3, valor1, valor2)
    else:
        print(valor3, valor2, valor1)