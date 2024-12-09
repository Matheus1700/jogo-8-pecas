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

        print("Novo estado após movimento:")
        for linha in vetor_jogo:
            print(linha)
        print("Distância de Manhattan para o objetivo:", menor_valor)
        print("--------------------------------")
        time.sleep(2)

    if vetor_jogo == objetivo:
        print("Objetivo alcançado!")

def formarAdjacentes(vetor_jogo):
    pos_adj = encontrarAdjacentes(vetor_jogo)
    linha_zero, coluna_zero = encontrarPosicaoZero(vetor_jogo)

    lista_resultado = []
    for linha_adj, coluna_adj in pos_adj:
        matriz_jogo = copy.deepcopy(vetor_jogo)

        # Troca os valores: o número adjacente ocupa o lugar do zero, e zero vai para a posição adjacente
        matriz_jogo[linha_zero][coluna_zero], matriz_jogo[linha_adj][coluna_adj] = (
            matriz_jogo[linha_adj][coluna_adj],
            matriz_jogo[linha_zero][coluna_zero],
        )

        lista_resultado.append(matriz_jogo)

    # Debug: exibir os estados adjacentes
    print("Estados adjacentes gerados:")
    for matriz in lista_resultado:
        for linha in matriz:
            print(linha)
        print("----------")

    return lista_resultado

def encontrarAdjacentes(vetor_jogo):
    linha_zero, coluna_zero = encontrarPosicaoZero(vetor_jogo)

    # Testamos todas as 4 direções possíveis
    direcoes = [
        (linha_zero, coluna_zero - 1),  # Esquerda
        (linha_zero, coluna_zero + 1),  # Direita
        (linha_zero - 1, coluna_zero),  # Cima
        (linha_zero + 1, coluna_zero),  # Baixo
    ]

    # Retornamos apenas as direções válidas
    posicoes_validas = [
        (linha, coluna)
        for linha, coluna in direcoes
        if 0 <= linha < 3 and 0 <= coluna < 3
    ]

    return posicoes_validas


def encontrarPosicaoZero(vetor_jogo):
    for i in range(3):
        for j in range(3):
            if vetor_jogo[i][j] == 0:
                return (i, j)



def busca_a_estrela(vetor_jogo):
    objetivo = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    
    # Fila de prioridade para gerenciar os estados
    fila_prioridade = []
    visitados = set()  # Para rastrear os estados já visitados

    # Adicionando o estado inicial
    custo_g = 0  # Custo acumulado g
    heuristica = distancia_manhattan(vetor_jogo)  # Estimativa da distância para o objetivo
    heapq.heappush(fila_prioridade, (custo_g + heuristica, custo_g, vetor_jogo))

    while fila_prioridade:
        _, custo_g, estado_atual = heapq.heappop(fila_prioridade)

        if estado_atual == objetivo:
            print("Objetivo alcançado!")
            return
        
        # Marcar estado como visitado
        estado_tuple = tuple(map(tuple, estado_atual))  # Converte para formato hashable
        if estado_tuple in visitados:
            continue
        visitados.add(estado_tuple)

        # Gerar os estados vizinhos
        vizinhos = formarAdjacentes(estado_atual)
        for vizinho in vizinhos:
            if tuple(map(tuple, vizinho)) not in visitados:
                novo_custo_g = custo_g + 1  # Incrementa o custo g
                nova_heuristica = distancia_manhattan(vizinho)  # Recalcula h(n)
                f_n = novo_custo_g + nova_heuristica  # Calcula f(n)
                heapq.heappush(fila_prioridade, (f_n, novo_custo_g, vizinho))

                # Exibição do progresso
                print("Novo estado após movimento:")
                for linha in vizinho:
                    print(linha)
                print(f"g(n): {novo_custo_g}, h(n): {nova_heuristica}, f(n): {f_n}")
                time.sleep(2)
                print("--------------------------------")

    print("Problema sem solução!")  # Caso a fila esvazie sem encontrar o objetivo


while True:
    # Gerando uma matriz inicial aleatória válida
    vetor_jogo = gerar_matriz_aleatoria()
    print("Gerando matriz\n")
    time.sleep(1)
    for linha in vetor_jogo:
        print(linha)
    print("--------------------------------")

    busca = input("Deseja uma demonstração de que tipo de busca?\n1- Busca Gulosa\n2- Busca A*\n")
    if busca == '1':
        busca_gulosa(vetor_jogo)
    elif busca == '2':
        busca_a_estrela(vetor_jogo)
    else:
        print("Opção inválida")
