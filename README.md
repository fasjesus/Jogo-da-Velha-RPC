# Jogo da Velha 5x5

<p align="justify">
    <strong>Jogo da Velha 5x5</strong> é um jogo de tabuleiro no estilo "cinco em linha" jogado em uma grade 5x5, onde dois jogadores competem para alinhar cinco peças consecutivas em linha reta, seja horizontal, vertical ou diagonal.<br><br>
    Este projeto implementa uma versão distribuída do jogo utilizando chamadas remotas de procedimento (RPC), permitindo que os jogadores se conectem e interajam em diferentes salas de jogo.
</p>

## Como Jogar?

<p align="justify">
    Para jogar, você precisará de pelo menos três terminais abertos: um para o servidor e dois para os jogadores.
</p>

### Configuração do Ambiente

<p align="justify">
Certifique-se de ter o Python 3.12 instalado. Os módulos utilizados fazem parte da biblioteca padrão do Python. Portanto não é necessário instalar módulos externos
</p>

### Rodando o Jogo

#### No Windows

Inicie o servidor:
```bash
python server.py
```
Em terminais separados, inicie os clientes:
```bash
python client.py
```
### Regras
<p align="justify">
    - O objetivo é alinhar cinco peças consecutivas em uma linha reta (horizontal, vertical ou diagonal).<br><br>
    - Dois jogadores se alternam para colocar suas peças na grade 5x5 até que um deles consiga alinhar cinco peças seguidas.
    <br><br>
    - Para fazer a jogada digite no seguinte formato:
</p>

```bash
linha coluna
```

