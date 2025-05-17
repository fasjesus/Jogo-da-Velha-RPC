#Aluno: Flávia Alessandra Santos dde Jesus.
import xmlrpc.server

# Classe para o jogo Gomoku
class JogoDaVelha:
    # Definição dos atributos da classe
    def __init__(self):
        self.tamanho = 5  # Tamanho do tabuleiro (5x5)
        self.tabuleiro = [[" " for _ in range(self.tamanho)] for _ in range(self.tamanho)] # Cria um tabuleiro vazio representado como uma matriz 5x5
        self.jogadores = [] # Lista de jogadores(Maximo de 2 jogadores)
        self.jogador_atual = 0  # Variável para guardar o jogador atual
        self.jogo_em_andamento = True # Variéavel para aber se o jogo acabou
        self.ultimo_movimento = None # Guarda o ultimo movimento

    # Função para registrar o jogador
    def registrar_jogador(self, nome):
        # Verifica se já tem dois jogadores registrados
        if len(self.jogadores) < 2:
            if nome in self.jogadores:
                return f"Jogador com o nome '{nome}' já registrado, escolha outro nome."

            self.jogadores.append(nome)
            return f"Jogador {nome} registrado com sucesso!"
        else:
            # Caso já existam dois jogadores o servidor envia um aviso para o jogador que tentou se cadastrar
            return "Já existem 2 jogadores registrados!"

    # Função para retornar a situação do jogo
    # Vai retorna o tabuleiro atualizado, o jogador atual e se o jogo está em andamento
    def obter_tabuleiro(self):
        return self.tabuleiro, self.jogador_atual, self.jogo_em_andamento

    # Retorna os dois jogadores cadastrados
    def obter_jogadores(self):
        return self.jogadores

    # Verifica o vencedor da partida
    def verificar_vencedor(self, linha, coluna):
        # Verifica combinações de 5 peças consecutivas
        direcoes = [
            (1, 0), (0, 1), (1, 1), (1, -1)  # Horizontal, vertical, diagonal esquerda e direita
        ]
        jogador = self.tabuleiro[linha][coluna]

        for dx, dy in direcoes:
            contador = 1 # Contador para a quantidade de X ou O iguais tem em cada direção
            # Verifica em uma direção
            for i in range(1, 5):
                x = coluna + dx * i
                y = linha + dy * i
                if 0 <= x < self.tamanho and 0 <= y < self.tamanho: # Verifica se as posições ainda estão dentro do range do tabuleiro
                    if self.tabuleiro[y][x] == jogador: # Verifica se a posição atual do tabuleiro pertence ao mesmo jogador d ajogada atual
                        contador += 1 # Incrementa 1 caso o jogador seja o mesmo
                    else:
                        break # Caso não seja ele sai do laço de repetição mais interno e checa em outra direção
            # Verifica na direção oposta
            for i in range(1, 5):
                x = coluna - dx * i
                y = linha - dy * i
                if 0 <= x < self.tamanho and 0 <= y < self.tamanho:
                    if self.tabuleiro[y][x] == jogador:
                        contador += 1
                    else:
                        break
            # Verifica se o contador tem 5 ou mais ocorrencias do mesmo jogador, caso tenha 5 ou mais ele ganha
            if contador >= 5:
                return True
        return False

    # Função para colocar a jogada do jogador no tabuleiro
    def movimento(self, jogador, linha, coluna):
        # Se o jogo estiver em andamento o codigo sera executado
        if self.jogo_em_andamento and self.jogadores[self.jogador_atual] == jogador:
            # Caso o jogador faça uma jogada invalida ele recebera uma mensagem de jogada invalida e terá que jogar de novo
            if (linha > 5 or linha < 0) or (coluna > 5 or coluna < 0):
                return "Posição invalida, jogue novamente!"
            else:
                # Verifica se a posição está vazia(não foi escolhida por algum jogador préviamente)
                if self.tabuleiro[linha][coluna] == " ":
                    self.tabuleiro[linha][coluna] = "X" if self.jogador_atual == 0 else "O" # Atribui "X" ou "O" a depender de qual é o jogador atual
                    self.ultimo_movimento = (jogador, linha, coluna) # Guarda o ultimo jogador e a posição que ele jogou

                    # Verifica se alguém venceu o jogo
                    if self.verificar_vencedor(linha, coluna):
                        self.jogo_em_andamento = False
                        return f"Jogador {jogador} venceu!"
                    elif all(self.tabuleiro[i][j] != " " for i in range(self.tamanho) for j in range(self.tamanho)): # Verifica se o jogo acabou em um empate
                        self.jogo_em_andamento = False
                        return "O jogo terminou em empate!"
                    else: # Caso ninguém tenha ganhado o servidor só vai enviar uma mensagem avisando que a jogada foi realizada com sucesso
                        self.jogador_atual = 1 - self.jogador_atual  # Variavel que vai alterar entre um jogador e outro
                        return "Movimento realizado com sucesso."
                else:
                    return "Posição já ocupada, jogue novamente!" # Caso o jogador tente jogar em uma posição já ocupada
        else:
            return "Não é o turno deste jogador." # Caso o jogador tente jogar fora da sua vez

# Iniciando o servidor RPC
servidor = xmlrpc.server.SimpleXMLRPCServer(("localhost", 8080)) # Seta o IP e a porta em que o servidor vai rodar
servidor.register_instance(JogoDaVelha()) # Registra uma instancia da classe Gomoku para o servidor usar
print("Servidor do Jogo da Velha RPC rodando...") # Mostra uma mansagem de que o servidor está rodando
servidor.serve_forever()