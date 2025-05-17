# Aluno: Flávia Alessandra Santos de Jesus.
import xmlrpc.client
import time

# Faz conexão com servidor locals
servidor = xmlrpc.client.ServerProxy("http://localhost:8080/")
# Pede para o usuário digitar o nome para se cadastrar
nome = input("Digite o seu nome para se registrar: ")
# Pega resposta do servidor para seber se o cadasstro foi feito corretamente
resposta_registro = servidor.registrar_jogador(nome)
# Imprime a resposta no terminal
print(resposta_registro)

# Função para imprimeir o tabuleiro formatado na tela
def imprimir_tabuleiro(tabuleiro):
    tamanho = len(tabuleiro) # Pega o tamanho do tabuleiro recebido da função
    linha_delimitadora = "+" + "---+" * tamanho  # Cria a linha delimitadora baseada no tamanho do tabuleiro
    j = 1 # Contador para a númeração de linhas qua vão se mostras na tela
    print("  1   2   3   4   5") # Imprime a númeração de colunas

    # Laço de repetição para gerar o tabuleiro
    for linha in tabuleiro:
        print(linha_delimitadora) # Imprime a linha delimitadora(+---+)
        # Cria a linha de células, separadas por "|"
        linha_formatada = "| " + " | ".join(celula if celula != " " else " " for celula in linha) + f" | {j}"
        print(linha_formatada) # Imprime a linha de células
        j = j + 1 # Incrementa o contador de linhas qua vão ser mostradas na tela
    print(linha_delimitadora)  # Linha final para fechar o tabuleiro

# Verifica se o registro ocorreu de forma correta
if "registrado com sucesso" in resposta_registro:
    jogo_em_andamento = True # Variável para saber se o jogo ainda está em andamento ou se acabou

    # Enquanto o jogo estiver em andamento o laço vai ser executado
    while jogo_em_andamento:
        # Pega o tabuleiro atualizado, jogador atual e estado do jogo
        tabuleiro, jogador_atual_servidor, jogo_em_andamento_servidor = servidor.obter_tabuleiro()

        # Mostrar o tabuleiro formatado
        print("\nTabuleiro atual:")
        imprimir_tabuleiro(tabuleiro) # Usa a função para imprimir o tabuleiro na tela

        # Se o jogo não estiver mais em andamento o laço de repetição é interrompido
        if not jogo_em_andamento_servidor:
            print("O jogo terminou!")
            break

        # Pega lista de jogadores para verificar quem é o jogador atual
        jogadores = servidor.obter_jogadores()

        # Caso seja a vez do jogador correto jogar o código será executado
        if nome == jogadores[jogador_atual_servidor]:
            print("É sua vez de jogar!")
            posicao = input("Digite a posição [Linha Coluna]: ") # Pega a posição na qual o jogador quer jogar, por exemplo(1 5), linha 1 e coluna 5, separados por um espaço
            linha, coluna = map(int, posicao.split()) # Como o input acima vai ser no formato de string, aqui vamos separas a string com base no espaço entre eles dois
            resultado = servidor.movimento(nome, linha - 1, coluna - 1) # Aqui o enviamos o nome do jogador e a posição que ele quer jogar par ao servidor
            print(resultado) # Aqui imprimimos o resultado o servidor

            # Se o jogador atual ganhar o jogo acaba, senão o a variável jogo_em_andamento contunua como True
            if "venceu" in resultado or "empate" in resultado:
                jogo_em_andamento = False
        else:
            # Caso não seja a vez do jogador jogar essa mensagem e o tebuleiro vão continuar sendo exubidos
            print("Aguardando o adversário...")

        # Espera 1 segundo para voltar ao topo do laço de repetição
        time.sleep(1)