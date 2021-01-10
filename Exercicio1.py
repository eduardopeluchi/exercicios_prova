def exercicio(parametro):
    contador = 0
    variavel_teste = 0
    resultado = 0
    lista_ordenada = sorted(parametro)

    while contador < len(lista_ordenada):
        testar_multiplos_tres = lista_ordenada[contador] % 3
        if testar_multiplos_tres == 0:
            if lista_ordenada[contador] > variavel_teste:
                variavel_teste = lista_ordenada[contador]

        resultado = variavel_teste
        contador += 1

    return resultado

lista_inteiros = [-6, -91, 1011, -100, 84, -22, 0, 1, 473]

print(exercicio(lista_inteiros))
