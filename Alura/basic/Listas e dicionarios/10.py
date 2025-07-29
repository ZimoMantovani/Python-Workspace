# 10) Um instituto de meteorologia deseja fazer um estudo de temperatura média de cada mês do ano. 
# Para isso, você precisa fazer um código que colete e armazene essas temperaturas médias em uma lista. 
# Depois, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual e em que mês elas ocorreram, 
# mostrando os meses por extenso (Janeiro, Fevereiro, etc.).

meses = [
	"Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
	"Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]
temp = []

for i in range(0, len(meses)):
    temperaturaMedia = float(input(f'Digite a temperatura de media do mês de {meses[i]}: '))
    temp.append(temperaturaMedia)

# Media anual
mediaAnual = sum(temp)/len(temp)
print(f'A media de temperatura foi de {mediaAnual}°C')

print('Meses que ultrapassaram a media: ')
for i in range(0, len(temp)):
    if(temp[i] > mediaAnual):
        print(f'{meses[i]} com {temp[i]}°C')
    