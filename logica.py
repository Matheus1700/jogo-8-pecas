# Aqui vai o codigo da manhattan distance
import copy


def formarAdjacentes(vetor_jogo, pos_zero, pos_adj):
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



vetor_jogo = [[1, 2, 3], [6, 8, 5], [7, 4, 0]]
lista_nova = formarAdjacentes(vetor_jogo, encontrarPosicaoZero(vetor_jogo), encontrarAdjacentes(vetor_jogo))

print("Lista Final: ")
print(lista_nova)