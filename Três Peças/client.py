# Flávia Alessandra Santos de Jesus.

# Programar um jogo da velha 5x5 distribuído para três jogadores remotos utilizando invocação de métodos remotos (RMI), 
# ou chamada de procedimentos remotos (RPC). A interface pode ser orientada a caracteres. Obs.: o jogo pode ser testado em um único computador.

import xmlrpc.client
import time

servidor = xmlrpc.client.ServerProxy("http://localhost:8080/")

nome = input("Digite o seu nome para se registrar: ")

resposta_registro = servidor.registrar_jogador(nome)
print(resposta_registro)

def imprimir_tabuleiro(tabuleiro):
    tamanho = len(tabuleiro)
    linha_delimitadora = "+" + "---+" * tamanho
    j = 1
    print("  " + "   ".join(str(i) for i in range(1, tamanho + 1)))
    for linha in tabuleiro:
        print(linha_delimitadora)
        linha_formatada = "| " + " | ".join(celula if celula != " " else " " for celula in linha) + f" | {j}"
        print(linha_formatada)
        j += 1
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
            except Exception:
                resultado = "Entrada inválida! Use formato: linha coluna (ex: 1 3)"
            print(resultado)

            if "venceu" in resultado or "empate" in resultado:
                jogo_em_andamento = False
        else:
            print("Aguardando o adversário...")

        time.sleep(1)
