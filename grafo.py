import os

def main():
    arquivo = open("A.txt", "r")
    conteudo = arquivo.readlines()
    arquivo.close()
    for n in range(len(conteudo)):
        conteudo[n] = conteudo[n].split()
    # Filtra a lista para remover itens vazios
    conteudo = list(filter(None, conteudo))

    existe, graus, soma = SeqGraus(conteudo)
    if not existe:
        exit()

    NArestas(soma)
    simples = GrafoSimples(conteudo)
    GrafoCompleto(conteudo, simples)
    GrafoRegular(graus)

    bipartido, x, y = GrafoBipartido(conteudo)
    GrafoBipartidoCompleto(simples, bipartido, x, y)


def SeqGraus(Matriz):  # Verifica a sequência dos graus do Grafo
    graus = []
    for linha in range(len(Matriz)):
        graus.append(0)
        for coluna in range(len(Matriz)):
            if linha == coluna:
                graus[linha] += (int(Matriz[linha][coluna])*2)
            else:
                graus[linha] += int(Matriz[linha][coluna])

    soma = 0
    for item in range(len(graus)):
        soma += graus[item]

    if soma % 2 == 1:
        print("O grafo não existe!")
        return False, graus, soma
    else:
        graus = decrescente(graus)
        print("Sequência dos graus do grafo:", end=" ")
        print(*graus, sep=", ")
        return True, graus, soma


def decrescente(graus):
    graus = sorted(graus)  # Organizar itens em ordem crescente
    graus = graus[::-1]  # Inverter a lista
    return graus


def NArestas(SomaGraus):  # Verifica o número de arestas do Grafo
    arestas = SomaGraus/2
    print("Número de arestas do grafo:", int(arestas))


def VerLacos(Matriz):  # Verifica se existem laços ou arestas múltiplas no grafo
    lacos = []
    Amultiplas = []

    for linha in range(len(Matriz)):
        # Duas estruturas de repetição para passar pelos itens da matriz
        for coluna in range(linha, len(Matriz)):
            # Se o valor da célula for maior que 0 ela é um laço
            if linha == coluna and int(Matriz[linha][coluna]) > 0:
                lacos.append("v{0}".format(linha+1))
            # Se o valor da célula for maior que 1 ela é aresta multipla
            elif int(Matriz[linha][coluna]) > 1:
                Amultiplas.append("v{0} e v{1}".format(linha+1, coluna+1))

    return lacos, Amultiplas


def GrafoSimples(Matriz):
    lacos, Amultiplas = VerLacos(Matriz)

    if lacos and Amultiplas:
        print("O grafo não é simples pois apresenta laços e arestas múltiplas")
        printLacos(lacos, Amultiplas)
        return False

    elif lacos or Amultiplas:
        if lacos:  # Se a lista não estiver vazia, o grafo tem laços
            print("O grafo não é simples pois apresenta laços")

        if Amultiplas:  # Se a lista não estiver vazia, o grafo tem Arestas Múltiplas
            print("O grafo não é simples pois apresenta arestas múltiplas")

        printLacos(lacos, Amultiplas)
        return False
    else:
        print("O grafo é simples pois não apresenta laços nem arestas multiplas!")
        return True


def printLacos(lacos, Amultiplas):
    if lacos:
        print("Vértices com laços:", end=" ")
        print(*lacos, sep=", ")
    else:
        print("O grafo não tem laços")

    if Amultiplas:
        print("Vértices com arestas múltiplas:", end=" ")
        print(*Amultiplas, sep=", ")
    else:
        print("O grafo não tem arestas múltiplas")


def GrafoCompleto(Matriz, simples):
    if not simples:
        completo = False
    else:
        completo = True
        for linha in range(len(Matriz)):
            for coluna in range(len(Matriz)):
                # Se o valor da célula for maior que 0 ela é um laço
                if linha == coluna and int(Matriz[linha][coluna]) != 0:
                    completo = False
                    break
                # Se o valor da célula for maior que 1 ela é aresta multipla
                elif linha != coluna and int(Matriz[linha][coluna]) != 1:
                    completo = False
                    break
    if completo:
        print("O grafo é completo? Sim")
    else:
        print("O grafo é completo? Não")


def GrafoRegular(graus):
    regular = True
    for item in graus:
        if graus[0] == item:
            pass
        else:
            regular = False
            break

    if regular:
        print("O grafo é regular? Sim")
    else:
        print("O grafo é regular? Não")


def GrafoBipartido(Matriz):
    x = [0]
    y = []
    bipar = True
    # Dar uma verificada sobre quando tiver laços
    for linha in range(len(Matriz)):
        for coluna in range(len(Matriz)):
            if linha in x and int(Matriz[linha][coluna]) != 0 and coluna not in y:
                if coluna in x:
                    bipar = False
                else:
                    y.append(coluna)
            elif linha in y and int(Matriz[linha][coluna]) != 0 and coluna not in x:
                if coluna in y:
                    bipar = False
                else:
                    x.append(coluna)
    if bipar:
        print("O grafo é bipartido? Sim")
        printbiparticao(x, y)
        return True, x, y
    else:
        print("O grafo é bipartido? Não")
        return False, False, False


def GrafoBipartidoCompleto(simples, bipartido, x, y):
    if simples and bipartido:
        print("O grafo é bipartido completo? Sim")
        printbiparticao(x, y)
    else:
        print("O grafo é bipartido completo? Não")


def printbiparticao(x, y):
    print("Bipartição:")
    print("X = {", end="")
    for v in x:
        if v == x[-1]:
            print("v{0}".format(v+1), end="}\n")
        else:
            print("v{0}".format(v+1), end=", ")

    print("Y = {", end="")
    for v in y:
        if v == y[-1]:
            print("v{0}".format(v+1), end="}\n")
        else:
            print("v{0}".format(v+1), end=", ")


main()
