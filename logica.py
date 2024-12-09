import copy
import random
import time
import heapq 


def distancia_manhattan(vetor_jogo):
    objetivo = ((1, 2, 3), (4, 5, 6), (7, 8, 0))
    distancia = 0

    for linha_atual in range(3): 
        for coluna_atual in range(3): 
            valor_atual = vetor_jogo[linha_atual][coluna_atual]

            if valor_atual != 0: 
                for linha_objetivo in range(3):  
                    for coluna_objetivo in range(3): 
                        if objetivo[linha_objetivo][coluna_objetivo] == valor_atual:
                            distancia += abs(linha_atual - linha_objetivo) + abs(coluna_atual - coluna_objetivo)
                            break

    return distancia

def gerar_matriz_aleatoria():
    matriz = list(range(9))
    while True:
        random.shuffle(matriz)
        matriz_2d = [matriz[:3], matriz[3:6], matriz[6:]]
        if matriz_resolvivel(matriz_2d):
            return matriz_2d

def matriz_resolvivel(matriz):
    lista = [num for linha in matriz for num in linha]
    inversoes = sum(1 for i in range(len(lista)) for j in range(i + 1, len(lista)) if lista[i] > lista[j] and lista[i] != 0 and lista[j] != 0)
    return inversoes % 2 == 0

def busca_gulosa(vetor_jogo):
    objetivo = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    visitados = set() 

    while vetor_jogo != objetivo:
        estado_atual = tuple(map(tuple, vetor_jogo))        
        visitados.add(estado_atual)  
        
        lista_nova = formarAdjacentes(vetor_jogo)
        distancias = []
        proximos_estados = []

        # calculando as distancias de Manhattan de todos os adj e filtrando posicoes já visitadas
        for e in lista_nova:
            estado_tuple = tuple(tuple(linha) for linha in e)
            if estado_tuple not in visitados:  
                dist = distancia_manhattan(e)
                distancias.append(dist)
                proximos_estados.append(e)

        if not proximos_estados:
            print("Ciclo detectado ou jogo não resolvido")
            break

        # Encontrando o estado com a menor distância
        menor_valor = min(distancias)
        posicao = distancias.index(menor_valor)
        vetor_jogo = proximos_estados[posicao]

        time.sleep(1)

        print("Novo estado:")
        for linha in vetor_jogo:
            print(linha)
        print("Distância de Manhattan para o objetivo:", menor_valor)
        print("--------------------------------")
        

    if vetor_jogo == objetivo:
        print("Objetivo alcançado!")

def formarAdjacentes(vetor_jogo):
    pos_adj = encontrarAdjacentes(vetor_jogo)
    pos_zero = encontrarPosicaoZero(vetor_jogo)

    linha_zero = pos_zero[0]
    coluna_zero = pos_zero[1]

    lista_resultado = list()
    for i in range(len(pos_adj)):
        matriz_jogo = copy.deepcopy(vetor_jogo)
        linha_adj, coluna_adj = pos_adj[i]          

        # trocando a posicao de 0 com o numero que vai substituilo
        matriz_jogo[linha_zero][coluna_zero] = matriz_jogo[linha_adj][coluna_adj] 

        # trocando o valor do numero adjacente por zero
        matriz_jogo[linha_adj][coluna_adj] = 0

        # adicionando na lista final
        lista_resultado.append(matriz_jogo)

    return lista_resultado

def encontrarAdjacentes(vetor_jogo):
    pos_zero = encontrarPosicaoZero(vetor_jogo)
    zero_x, zero_y = pos_zero
    pos_testadas = [(zero_x, zero_y - 1), (zero_x, zero_y + 1), 
                    (zero_x - 1, zero_y), (zero_x + 1, zero_y)]
    
    pos_adj = []
    for linha_atual, coluna_atual in pos_testadas:
        if linha_atual >= 0 and coluna_atual >= 0:  # Exclui posições fora da matriz
            try:
                valor = vetor_jogo[linha_atual][coluna_atual]
                pos_adj.append((linha_atual, coluna_atual))
            except IndexError:
                pass

    return pos_adj

def encontrarPosicaoZero(vetor_jogo):
    for i in range(3):
        for j in range(3):
            if vetor_jogo[i][j] == 0:
                return (i, j)

def busca_a_estrela(vetor_jogo):
    objetivo = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    visitados = set()  # Estados já visitados

    # Fila de prioridade para armazenar os estados no formato (f, g, estado)
    fila = []
    heapq.heappush(fila, (0, 0, vetor_jogo))  

    while fila:
        _, g, estado_atual = heapq.heappop(fila)
        estado_tuple = tuple(map(tuple, estado_atual))

        if estado_atual == objetivo:
            print("Objetivo alcançado!")
            for linha in estado_atual:
                print(linha)
            return

        # Marca o estado como visitado
        if estado_tuple in visitados:
            continue
        visitados.add(estado_tuple)

        lista_nova = formarAdjacentes(estado_atual)

        for e in lista_nova:
            estado_tuple_novo = tuple(map(tuple, e))
            if estado_tuple_novo not in visitados:
                h = distancia_manhattan(e)  
                f = g + 1 + h  # Cálculo de f(n)
                heapq.heappush(fila, (f, g + 1, e))  

        time.sleep(1)

        print("Estado atual:")
        for linha in estado_atual:
            print(linha)
        print(f"Custo acumulado (g): {g}, Heurística (h): {distancia_manhattan(estado_atual)}")
        print("--------------------------------")

    print("O problema não tem solução ou não foi resolvido.")



# Gerando uma matriz inicial aleatória válida
vetor_jogo = gerar_matriz_aleatoria()
print("Matriz inicial:")
for linha in vetor_jogo:
    print(linha)
print("--------------------------------")


resposta = input("1 - Busca Gulosa \n2 - Busca A*")
if resposta == 1:
    busca_gulosa(vetor_jogo)
else:
    busca_a_estrela(vetor_jogo)
