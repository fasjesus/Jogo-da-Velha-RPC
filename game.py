# Flávia Alessandra Santos de Jesus.
class JogoDaVelha:
    def __init__(self):
        self.tamanho = 5
        self.tabuleiro = [[" " for _ in range(self.tamanho)] for _ in range(self.tamanho)]
        self.jogadores = []
        self.jogador_atual = 0
        self.jogo_em_andamento = True
        self.ultimo_movimento = None

    def registrar_jogador(self, nome):
        if len(self.jogadores) < 2:
            if nome in self.jogadores:
                return f"Jogador com o nome '{nome}' já registrado, escolha outro nome."
            self.jogadores.append(nome)
            return f"Jogador {nome} registrado com sucesso!"
        return "Já existem 2 jogadores registrados!"

    def obter_tabuleiro(self):
        return self.tabuleiro, self.jogador_atual, self.jogo_em_andamento

    def obter_jogadores(self):
        return self.jogadores

    def verificar_vencedor(self, linha, coluna):
        direcoes = [(1, 0), (0, 1), (1, 1), (1, -1)]
        jogador = self.tabuleiro[linha][coluna]

        for dx, dy in direcoes:
            contador = 1
            for i in range(1, 5):
                x, y = coluna + dx * i, linha + dy * i
                if 0 <= x < self.tamanho and 0 <= y < self.tamanho:
                    if self.tabuleiro[y][x] == jogador:
                        contador += 1
                    else:
                        break
            for i in range(1, 5):
                x, y = coluna - dx * i, linha - dy * i
                if 0 <= x < self.tamanho and 0 <= y < self.tamanho:
                    if self.tabuleiro[y][x] == jogador:
                        contador += 1
                    else:
                        break
            if contador >= 5:
                return True
        return False

    def movimento(self, jogador, linha, coluna):
        if self.jogo_em_andamento and self.jogadores[self.jogador_atual] == jogador:
            if not (0 <= linha < self.tamanho and 0 <= coluna < self.tamanho):
                return "Posição inválida, jogue novamente!"
            if self.tabuleiro[linha][coluna] != " ":
                return "Posição já ocupada, jogue novamente!"

            self.tabuleiro[linha][coluna] = "X" if self.jogador_atual == 0 else "O"
            self.ultimo_movimento = (jogador, linha, coluna)

            if self.verificar_vencedor(linha, coluna):
                self.jogo_em_andamento = False
                return f"Jogador {jogador} venceu!"
            elif all(self.tabuleiro[i][j] != " " for i in range(self.tamanho) for j in range(self.tamanho)):
                self.jogo_em_andamento = False
                return "O jogo terminou em empate!"

            self.jogador_atual = 1 - self.jogador_atual
            return "Movimento realizado com sucesso."
        return "Não é o turno deste jogador."
