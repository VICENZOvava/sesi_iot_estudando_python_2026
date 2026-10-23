
with open("entrada.txt", "r") as entrada:
    with open("saida.txt", "w") as saida:
        while True:
            linha = entrada.readline()

            if not linha:
                break

            N, F = map(int, linha.split())

            if N == 0 and F == 0:
                break

            volume = (F * 50) / (N * 1000)

            saida.write(f"{volume:.2f}\n")
