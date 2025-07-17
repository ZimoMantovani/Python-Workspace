# 2) Escreva um programa que solicite o percentual de crescimento de produção de uma empresa e informe se houve um crescimento (porcentagem positiva) ou decrescimento (porcentagem negativa).

crescimento = float(input('Digite o percentual de crescimento de produção: '))
if crescimento > 0:
    print("Houve crescimento na produção.")
elif crescimento < 0:
    print("Houve decrescimento na produção.")
else:
    print("A produção permaneceu igual.")
