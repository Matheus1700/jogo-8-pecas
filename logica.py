# Aqui vai o codigo da manhattan distance
import copy

# calculando distancias iguais -- ERRO
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


def busca_gulosa(vetor_jogo):
    pass


def formarAdjacentes(vetor_jogo):
    pos_adj = encontrarAdjacentes(vetor_jogo)
    pos_zero = encontrarPosicaoZero(vetor_jogo)

    linha_zero = pos_zero[0]
    coluna_zero = pos_zero[1]

    lista_resultado = list()
    for i in range(len(pos_adj)):
        matriz_jogo = copy.deepcopy(vetor_jogo)
        linha_adj = pos_adj[i][0];  coluna_adj = pos_adj[i][1];

        # trocando a posicao de 0 com o numero que vai substituilo
        matriz_jogo[linha_zero][coluna_zero] = matriz_jogo[linha_adj][coluna_adj] 

        # trocando o valor do numero adjacente por zero
        matriz_jogo[linha_adj][coluna_adj] = 0

        # adicionando na lista final
        lista_resultado.append(matriz_jogo)

    return lista_resultado

def encontrarAdjacentes(vetor_jogo):             #  x  y 
    pos_zero = encontrarPosicaoZero(vetor_jogo)  # (1, 1)  -->      Linha                                 Superior
                                                    # (1, 0) ,  (1, 2)                      , (0, 1), (2, 1)
                                                    # (x, (y - 1)), (x, (y + 1))        ((x - 1), y), ((x + 1), y)
    zero_x = pos_zero[0];   zero_y = pos_zero[1]
    pos_testadas = ((zero_x, (zero_y - 1)), (zero_x, (zero_y + 1)), 
                    (zero_x -1, zero_y), (zero_x + 1, zero_y));
    
    pos_adj = []
    for i in range(4):
        linha_atual = pos_testadas[i][0];
        coluna_atual = pos_testadas[i][1];

        if (linha_atual >= 0) and (coluna_atual >= 0): # exclui posicoes com valores negativos
            try:
                valor = vetor_jogo[linha_atual][coluna_atual]
                pos_adj.append((linha_atual, coluna_atual))
            except IndexError:
                pass

    return pos_adj;

def encontrarPosicaoZero(vetor_jogo):
     pos_zero = tuple()

     for i in range (3):
        for j in range (3):
            if (vetor_jogo[i][j] == 0):
                pos_zero = (i, j)
                return pos_zero



vetor_jogo = [[1, 2, 3], [5, 0, 4], [7, 8, 9]]
lista_nova = formarAdjacentes(vetor_jogo)

print("Lista Final: ")
for e in lista_nova:
    print(e)
print("--------------------------------")
print("Distancia: ", distancia_manhattan(lista_nova[0]))
print("Distancia: ", distancia_manhattan(lista_nova[1]))
print("Distancia: ", distancia_manhattan(lista_nova[2]))
print("Distancia: ", distancia_manhattan(lista_nova[3]))