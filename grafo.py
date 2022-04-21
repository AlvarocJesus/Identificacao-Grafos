arquivo = open('./A.txt', 'r')
matriz = []
sequency = []
simples = 0
laco = []
multAresta = []
n = 0

for i in arquivo.readlines():
	matriz.append(i.strip().split())
matriz.pop()
# print(matriz)

# Verifica se o grafo e simples
for linha in range(len(matriz)):
	for coluna in range(len(matriz[linha])):
		# print('%s' % matriz[linha][coluna], end=' ')
		sequency.append(matriz[linha][coluna])
		if(int(matriz[linha][coluna]) == 1):
			simples += 1
			# print(f'Simples: {simples}')
	# print()
	n+=1
	print(f'N: {n}')

# Verifica se existe laco
for linha in range(len(matriz)):
	for coluna in range(len(matriz[linha])):
		if((linha == coluna) and (int(matriz[linha][coluna]) >= 1)):
			laco.append('No vertice v%d, existe um laco de grau %s' %(linha+1, matriz[linha][coluna]))
		elif ((linha != coluna) and (int(matriz[linha][coluna]) > 1)):
			multAresta.append('No vertice v%d, existe mais de uma aresta, assim possuindo grau %s' % (linha+1, matriz[linha][coluna]))

complete = (n * (n-1))/2
print(f'Complete: {n-1}')


print(simples)
if(simples == 11):
	print('O grafo e simples e completo\n')
	print(simples)
else:
	print('O grafo nao e simples e completo\n')
	# print(simples)

print('Vertices com laços:')
for i in range(len(laco)):
	print(laco[i])
print()

print('Vertices com arestas múltiplas:')
for i in range(len(multAresta)):
	print(multAresta[i])
print()

ordenada = sorted(sequency, reverse=True)
print('Sequencia dos graus: { %s }\n' % ', '.join(ordenada))
print(f'Quantidade de arestas: {len(matriz)}')
