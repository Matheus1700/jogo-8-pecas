import tkinter as tk

# Criar a janela principal
root = tk.Tk()
root.title("8-Puzzle")

# Variáveis globais
vazio_pos = [2, 2]  # Posição inicial do espaço vazio

# Função para movimentar uma peça
def mover_peca(linha, coluna):
    global vazio_pos

    # Verificar se a peça clicada está adjacente ao espaço vazio
    linha_vazio, coluna_vazio = vazio_pos
    if (abs(linha - linha_vazio) == 1 and coluna == coluna_vazio) or \
       (abs(coluna - coluna_vazio) == 1 and linha == linha_vazio):

        # Trocar o texto do botão clicado com o do espaço vazio
        idx_vazio = linha_vazio * 3 + coluna_vazio
        idx_clicado = linha * 3 + coluna

        buttons[idx_vazio]["text"], buttons[idx_clicado]["text"] = \
            buttons[idx_clicado]["text"], buttons[idx_vazio]["text"]

        # Atualizar a posição do espaço vazio
        vazio_pos = [linha, coluna]

# Criar o frame para o grid
frame_grid = tk.Frame(root)
frame_grid.pack()

# Criar os botões das peças
buttons = []
for i in range(3):
    row = []
    for j in range(3):
        if i == 2 and j == 2:
            button = tk.Button(frame_grid, text="", width=5, height=2, bg="white",
                               command=lambda linha=i, coluna=j: mover_peca(linha, coluna))
        else:
            button = tk.Button(frame_grid, text=str(i * 3 + j + 1), width=5, height=2, bg="white",
                               command=lambda linha=i, coluna=j: mover_peca(linha, coluna))
        button.grid(row=i, column=j)
        row.append(button)
    buttons.extend(row)

# Criar os botões de controle
frame_buttons = tk.Frame(root)
frame_buttons.pack()
button_embaralhar = tk.Button(frame_buttons, text="Embaralhar", command=lambda: None)
button_gulosa = tk.Button(frame_buttons, text="Busca Gulosa", command=lambda: None)
button_aestrela = tk.Button(frame_buttons, text="Busca A*", command=lambda: None)
button_embaralhar.pack(side="left")
button_gulosa.pack(side="left")
button_aestrela.pack(side="left")








# Iniciar a aplicação
root.mainloop()