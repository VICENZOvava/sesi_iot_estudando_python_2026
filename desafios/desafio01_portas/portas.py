
with open("entrada.txt", "r") as entrada:
    with open("saida.txt", "w") as saida:
        for linha in entrada:
            N = int(linha)

            if N == 0:
                break

            portas = []

            i = 1
            while i * i <= N:
                portas.append(str(i * i))
                i += 1

            saida.write(" ".join(portas) + "\n")
