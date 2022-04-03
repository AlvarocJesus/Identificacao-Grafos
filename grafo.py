arquivo = open('./A.txt', 'r')
matriz = []
sequency = []
vertices = 0

for i in arquivo.readlines():
    matriz.append(i.strip().split())

# print(matriz)

for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        # print('%s' % matriz[linha][coluna], end=' ')
        sequency.append(matriz[linha][coluna])
        if(int(matriz[linha][coluna]) >= 1):
            vertices += 1
    # print()

if(vertices == 11):
    print('O grado e simples')
    print(vertices)
else:
    print('O grafo nao e simples')
    print(vertices)
ordenada = sorted(sequency, reverse=True)
print('Sequencia dos graus: { %s }' % ', '.join(ordenada))
print(f'Quantidade de arestas: {len(matriz)}')
