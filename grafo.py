arquivo = open('./A.txt', 'r')
matriz = []

for i in arquivo.readlines():
    matriz.append(i.strip().split())

print(matriz)

for linha in range(len(matriz)):
	for coluna in range(len(matriz[linha])):
		print('%s' % matriz[linha][coluna], end=' ')
	print()
