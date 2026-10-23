
with open("entrada.txt", "r") as entrada:
    with open("saida.txt", "w") as saida:
        while True:
            linha = entrada.readline()

            if not linha:
                break

            N = int(linha)

            if N == 0:
                break

            erros = {}
            resolvidos = set()
            problemas = {}

            for _ in range(N):
                problema, tempo, julgamento = entrada.readline().split()
                tempo = int(tempo)

                if problema in resolvidos:
                    continue

                if julgamento == "incorrect":
                    erros[problema] = erros.get(problema, 0) + 1
                else:
                    resolvidos.add(problema)
                    problemas[problema] = tempo

            S = len(resolvidos)
            P = 0

            for problema in resolvidos:
                P += problemas[problema]
                P += erros.get(problema, 0) * 20

            saida.write(f"{S} {P}\n")
