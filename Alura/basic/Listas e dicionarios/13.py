# 13) As pessoas colaboradoras de um setor da empresa que você trabalha vão receber um abono correspondente a 10% do salário devido 
# ao ótimo desempenho do time. O setor financeiro solicitou sua ajuda para a verificação das consequências financeiras que esse abono 
# irá gerar nos recursos. Assim, foi encaminhada para você uma lista com os salários que receberão o abono: 
# [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]. O abono de cada colaborador(a) não pode ser inferior a 200. 
# Em código, transforme cada um dos salários em chaves de um dicionário e o abono de cada salário no elemento. 
# Depois, informe o total de gastos com o abono, quantos(as) colaboradores(as) receberam o abono mínimo e qual o maior valor de abono fornecido.

salarios = {
    'salario1': 1172,
    'salario2': 1644,
    'salario3': 2617,
    'salario4': 5130,
    'salario5': 5532,
    'salario6': 6341,
    'salario7': 6650,
    'salario8': 7238,
    'salario9': 7685,
    'salario10': 7782,
    'salario11': 7903
}
salarioValor = list(salarios.values())
abonoLista = []
cont = 0
for i in range(0, len(salarios)):
    abono = salarioValor[i] * 0.1 
    
    if(abono < 200):
        abono = 200
        cont += 1
    
    abonoLista.append(abono)



print(f'{cont} usuarios receberam o valor minimo e o maior abono foi de {max(abonoLista)}')