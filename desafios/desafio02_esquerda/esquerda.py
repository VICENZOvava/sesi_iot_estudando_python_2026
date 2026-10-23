
with open("entrada.txt", "r") as entrada:
    with open("saida.txt", "w") as saida:
        while True:
            N = int(entrada.readline())

            if N == 0:
                break

            comandos = entrada.readline().strip()

            direcoes = ["N", "L", "S", "O"]
            posicao = 0

            for comando in comandos:
                if comando == "D":
                    posicao = (posicao + 1) % 4
                else:
                    posicao = (posicao - 1) % 4

            saida.write(direcoes[posicao] + "\n")
