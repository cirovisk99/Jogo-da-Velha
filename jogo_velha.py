# Função para imprimir o tabuleiro
def imprimir_tabuleiro(tabuleiro):
    print("\n  Jogo da Velha")
    print("-------------")
    for i in range(3):
        print(f"| {tabuleiro[i][0]} | {tabuleiro[i][1]} | {tabuleiro[i][2]} |")
        print("-------------")

# Função para verificar se um jogador venceu
def verificar_vitoria(tabuleiro, jogador):
    # Verificar linhas
    for i in range(3):
        if all([tabuleiro[i][j] == jogador for j in range(3)]):
            return True
    # Verificar colunas
    for j in range(3):
        if all([tabuleiro[i][j] == jogador for i in range(3)]):
            return True
    # Verificar diagonais
    if all([tabuleiro[i][i] == jogador for i in range(3)]) or \
       all([tabuleiro[i][2-i] == jogador for i in range(3)]):
        return True
    return False

# Função para verificar se houve empate
def verificar_empate(tabuleiro):
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == ' ':
                return False
    return True

# Função principal do jogo
def jogo_da_velha():
    tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
    jogador_atual = 'X'
    jogo_ativo = True

    while jogo_ativo:
        imprimir_tabuleiro(tabuleiro)
        print(f"É a vez do jogador: {jogador_atual}")

        while True:
            try:
                linha = int(input("Digite a linha (1-3): ")) - 1
                coluna = int(input("Digite a coluna (1-3): ")) - 1

                if 0 <= linha < 3 and 0 <= coluna < 3 and tabuleiro[linha][coluna] == ' ':
                    tabuleiro[linha][coluna] = jogador_atual
                    break
                else:
                    print("Posição inválida ou já ocupada. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")

        if verificar_vitoria(tabuleiro, jogador_atual):
            imprimir_tabuleiro(tabuleiro)
            print(f"Parabéns! O jogador '{jogador_atual}' venceu!")
            jogo_ativo = False
        elif verificar_empate(tabuleiro):
            imprimir_tabuleiro(tabuleiro)
            print("O jogo terminou em empate!")
            jogo_ativo = False
        else:
            jogador_atual = 'O' if jogador_atual == 'X' else 'X'

# Inicia o jogo
jogo_da_velha()