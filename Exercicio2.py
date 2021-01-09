def exercicio2(parametro1, paramentro2):
    resultado_multiplicacao = parametro1 * paramentro2
    resultado_multiplicacao_bin = list(bin(resultado_multiplicacao))
    contador = 2
    resultado_somas_um_binario = 0

    while contador < len(resultado_multiplicacao_bin):

        if int(resultado_multiplicacao_bin[contador]) == 1:
            resultado_somas_um_binario += 1

        contador += 1

    print(resultado_somas_um_binario)


exercicio2(3, 7)
