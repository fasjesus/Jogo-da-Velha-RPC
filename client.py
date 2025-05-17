# Flávia Alessandra Santos de Jesus.
import xmlrpc.client
import time

servidor = xmlrpc.client.ServerProxy("http://localhost:8080/")
nome = input("Digite o seu nome para se registrar: ")
resposta_registro = servidor.registrar_jogador(nome)
print(resposta_registro)

def imprimir_tabuleiro(tabuleiro):
    tamanho = len(tabuleiro)
    linha_delimitadora = "+" + "---+" * tamanho
    print("  " + "   ".join(str(i + 1) for i in range(tamanho)))

    for i, linha in enumerate(tabuleiro):
        print(linha_delimitadora)
        linha_formatada = "| " + " | ".join(c if c != " " else " " for c in linha) + f" | {i + 1}"
        print(linha_formatada)
    print(linha_delimitadora)

if "registrado com sucesso" in resposta_registro:
    jogo_em_andamento = True
    while jogo_em_andamento:
        tabuleiro, jogador_atual_servidor, jogo_em_andamento_servidor = servidor.obter_tabuleiro()
        print("\nTabuleiro atual:")
        imprimir_tabuleiro(tabuleiro)

        if not jogo_em_andamento_servidor:
            print("O jogo terminou!")
            break

        jogadores = servidor.obter_jogadores()
        if nome == jogadores[jogador_atual_servidor]:
            print("É sua vez de jogar!")
            posicao = input("Digite a posição [Linha Coluna]: ")
            try:
                linha, coluna = map(int, posicao.split())
                resultado = servidor.movimento(nome, linha - 1, coluna - 1)
                print(resultado)
                if "venceu" in resultado or "empate" in resultado:
                    jogo_em_andamento = False
            except ValueError:
                print("Formato inválido! Digite dois números separados por espaço.")
        else:
            print("Aguardando o adversário...")

        time.sleep(1)
