'''
Em uma empresa de venda de imóveis você precisa criar um código que analise os dados de vendas anuais para ajudar a diretoria na tomada de decisão.
O código precisa coletar os dados de quantidade de venda durante os anos de 2022 e 2023 e fazer um cálculo de variação percentual.
A partir do valor da variação, deve ser enviada às seguintes sugestões:

Para variação acima de 20%: bonificação para o time de vendas.
Para variação entre 2% e 20%: pequena bonificação para time de vendas.
Para variação entre 2% e -10%: planejamento de políticas de incentivo às vendas.
Para bonificações abaixo de -10%: corte de gastos.
'''

vendas2022 = float(input('Digite a quantidade vendida em 2022: '))
vendas2023 = float(input('Digite a quantidade vendida em 2023: '))

aux = vendas2023*100
percentual = (aux/vendas2022)-100
print(f'Foram vendidos {percentual}% comparado com ano passado')

if(percentual > 20):
    print('Parabéns! Bonificação a todos')
elif(percentual > 2 and percentual < 20):
    print('Pequena bonificação para time de vendas')
elif(percentual >-10  and percentual < 2 ):
    print('Planejamento de políticas de incentivo às vendas')
else:
    print('corte de gastos')