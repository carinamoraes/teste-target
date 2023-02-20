import json

with open("dados.json", encoding='utf-8') as meu_json:
    dados = json.load(meu_json)

dias = []
valores = []
media = 0

for i in dados:
    dias.append(i['dia'])
    valores.append(i['valor'])

menor_valor = min(valores)
dia_menor_valor = dias[valores.index(menor_valor)]
maior_valor = max(valores)
dia_maior_valor = dias[valores.index(maior_valor)]

print("Menor valor de faturamento: ", menor_valor, " Dia do mês: ", dia_menor_valor,
"\nMaior valor de faturamento: ", maior_valor, " Dia do mês: ", dia_maior_valor)

total = 0
total_dias = 0

for i in valores:
    if i != 0:
        total += i
        total_dias +=1

media = total / total_dias

dia_aux = 0

for i in valores:
    if i > media:
        dia_aux += 1

print("Média mensal: ", media, "\nNúmero de dias no mês em que o valor de faturamento diário foi superior à média mensal: ", dia_aux)
