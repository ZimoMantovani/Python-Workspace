# 2) Escreva um programa para calcular quantos dias levará para a colônia de uma bactéria A 
# ultrapassar ou igualar a colônia de uma bactéria B, com base nas taxas de crescimento de 3% e 1,5% respectivamente. 
# Considere que a colônia A inicia com 4 elementos e a B com 10.

coloniaA = 4.0
coloniaB = 10.0
cont = 0

while coloniaA <= coloniaB:
    coloniaA = coloniaA+(coloniaA*0.03)
    coloniaB = coloniaB+(coloniaB*0.015)
    
    print(f'A:',coloniaA)
    print(f'B:',coloniaB,'\n')
    cont += 1
print(f'Foram necessarios {cont} dias para a colonia A ultrapassar a B')