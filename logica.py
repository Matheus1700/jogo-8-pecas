# Aqui vai o codigo da manhattan distance

def encontrarAdjacentes(vetor_jogo):    # x  y 
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
                print(valor)
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



vetor_jogo = [[1, 2, 3], (6, 8, 5), (7, 4, 0)]
print("Adjacentes do Zero: ", encontrarAdjacentes(vetor_jogo))
print("Posicao do Zero: ", encontrarPosicaoZero(vetor_jogo))