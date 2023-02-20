def calcula_fibonacci(numero):
    fibonacci = [0, 1]

    valor = 0

    while valor <= numero:
        tamanho = len(fibonacci)
        valor = fibonacci[tamanho - 1] + fibonacci[tamanho - 2]
        fibonacci.append(valor)

    aux = 0

    for i in fibonacci:
        if i == numero:
            aux = 1

    if aux == 1: print("Pertence.")
    else: print("Não pertence.")
            
    
numero = int(input("Informe um número: "))
calcula_fibonacci(numero)