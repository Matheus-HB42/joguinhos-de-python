import random


def jogar():
    print("**" * 20)
    print("O QUÃO BOM VOCE É EM CHUTE")
    print("**" * 20)
    pontos = 1000
    tentativas = 0
    numero_secreto = random.randrange(1, 101)

    # definindo a dificuldade
    print("Qual o nível de dificildade?")
    nivel = int(input("1 = Facil, 2 = Médio, 3 = Difícil"))

    if nivel == 1:
        tentativas = 20
    elif nivel == 2:
        tentativas = 10
    else:
        tentativas = 5

    # criando um loop detalhe na linha 33 diminuindo o valor das rodadas
    for rodada in range(1, tentativas + 1):
        # mostrando a quantidade de tentativas / rodadas
        print(" Tentativa {} de {}".format(rodada, tentativas))
        # se na ultima rodada mostra uma mnsg de aviso
        if rodada == tentativas:
            print("=-" * 10)
            print("CUIDADO ESSA É A ULTIMA TENTATIVA")
            print("-=" * 10)
        # perguntando o numero do jogador
        chute = int(input("Chute um valor entre 1 e 100!!"))
        if chute < 1 or chute > 100:
            print("Apenas valores entre 1 e 100")
            # com o continue se o usuario digitar um valor fora do range ele perde uma rodada(bloqueia a interação do usuario)
            continue
        print("Voce chutou... {}".format(chute))
        # aqui a condição se o jogador acertar
        if chute == numero_secreto:
            if rodada == tentativas:
                print("Foi na ultima mais ainda assim ta valendo... BOA!!")
                print("E finalizou com {} pontos".format(pontos))
            print("Parabens!!  Você acertou o valor")
            print("Conseguiu {} pontos".format(pontos))
            # com o break se o usuario acertar o valor o programa nao continua rodando (bloqueia o loop completo)
            break
            # aqui se acertar na ultima rodada
        else:

            # condicao se o jogador chutar um valor abaixo q o numero definido
            if chute < numero_secreto:
                print("Esta quase mas n é esse, tente algo um pouco mais pra cima")
                if rodada == tentativas:
                    print("O numero era {}".format(numero_secreto))
            # condiçao se o jogador chutar um valor acima do numero definido
            elif chute > numero_secreto:
                print("Passoooou... tente um pouco mais a baixo")
                if rodada == tentativas:
                    print("O numero era {}".format(numero_secreto))
        # a função abs() aqui serve para retirar o numero absoluto (o numero sem o sinal)
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos
        print("**" * 30)

    print("**" * 10)
    print("FIM DE JOGO")
    print("**" * 10)


if __name__ == "__main__":
    jogar()
