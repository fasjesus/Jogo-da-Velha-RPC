# Flávia Alessandra Santos de Jesus.

import xmlrpc.server

class JogoDaVelha:
    def __init__(self):
        self.tamanho = 5
        self.tabuleiro = [[" " for _ in range(self.tamanho)] for _ in range(self.tamanho)]
        self.jogadores = []  # até 3 jogadores agora
        self.jogador_atual = 0
        self.jogo_em_andamento = True
        self.ultimo_movimento = None
        self.simbolos = ["X", "O", "Y"]  # símbolos para 3 jogadores

    def registrar_jogador(self, nome):
        if len(self.jogadores) < 3:
            if nome in self.jogadores:
                return f"Jogador com o nome '{nome}' já registrado, escolha outro nome."
            self.jogadores.append(nome)
            return f"Jogador {nome} registrado com sucesso!"
        else:
            return "Já existem 3 jogadores registrados!"

    def obter_tabuleiro(self):
        return self.tabuleiro, self.jogador_atual, self.jogo_em_andamento

    def obter_jogadores(self):
        return self.jogadores

    def verificar_vencedor(self, linha, coluna):
        direcoes = [
            (1, 0), (0, 1), (1, 1), (1, -1)
        ]
        jogador = self.tabuleiro[linha][coluna]

        for dx, dy in direcoes:
            contador = 1
            for i in range(1, 5):
                x = coluna + dx * i
                y = linha + dy * i
                if 0 <= x < self.tamanho and 0 <= y < self.tamanho:
                    if self.tabuleiro[y][x] == jogador:
                        contador += 1
                    else:
                        break
                else:
                    break
            for i in range(1, 5):
                x = coluna - dx * i
                y = linha - dy * i
                if 0 <= x < self.tamanho and 0 <= y < self.tamanho:
                    if self.tabuleiro[y][x] == jogador:
                        contador += 1
                    else:
                        break
                else:
                    break
            if contador >= 5:
                return True
        return False

    def movimento(self, jogador, linha, coluna):
        if not self.jogo_em_andamento:
            return "O jogo já acabou!"

        if self.jogadores[self.jogador_atual] != jogador:
            return "Não é o turno deste jogador."

        if linha < 0 or linha >= self.tamanho or coluna < 0 or coluna >= self.tamanho:
            return "Posição inválida, jogue novamente!"

        if self.tabuleiro[linha][coluna] != " ":
            return "Posição já ocupada, jogue novamente!"

        simbolo = self.simbolos[self.jogador_atual]
        self.tabuleiro[linha][coluna] = simbolo
        self.ultimo_movimento = (jogador, linha, coluna)

        if self.verificar_vencedor(linha, coluna):
            self.jogo_em_andamento = False
            return f"Jogador {jogador} venceu!"

        # Verifica empate (tabuleiro cheio)
        if all(self.tabuleiro[i][j] != " " for i in range(self.tamanho) for j in range(self.tamanho)):
            self.jogo_em_andamento = False
            return "O jogo terminou em empate!"

        # Passa para o próximo jogador (0,1,2,0,1,2,...)
        self.jogador_atual = (self.jogador_atual + 1) % 3

        return "Movimento realizado com sucesso."

# Iniciando o servidor
servidor = xmlrpc.server.SimpleXMLRPCServer(("localhost", 8080))
servidor.register_instance(JogoDaVelha())
print("Servidor do Jogo da Velha 5x5 (Para 5 Peças) RPC rodando...")
servidor.serve_forever()

