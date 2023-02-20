estados = ['SP', 'RJ', 'MG', 'ES', 'Outros']
faturamento = [67836.43, 36678.66, 29229.88, 27165.48, 19849.53]
representacao = []

total = sum(faturamento)

for i in faturamento:
    rep = (i * 100) / total
    representacao.append(round(rep))



print("Total: ", total,"\nPercentual de representação de estado: ")

for i in representacao:
    print(estados[representacao.index(i)],"-" ,i,"%\n")