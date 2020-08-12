import random


def jogar():
    começo()
    palavra_secreta = seleção_palavra()

    letras_certas = ["_" for letra in palavra_secreta]
    print(letras_certas)

    enforcou = False
    acertou = False
    erros = 0

    while not acertou and not enforcou:
        chute = pede_chute()

        letras_faltando = letras_que_faltam(letras_certas, palavra_secreta, chute)

        if chute in palavra_secreta:
            maraca_chute_certo(palavra_secreta, chute, letras_certas)
        else:
            erros += 1
            desenha_forca(erros)
            print("Ops, você errou! faltam mais {} tentativas".format(7 - erros))

        enforcou = erros == 7
        acertou = "_" not in letras_certas
        print(letras_certas)
        if letras_faltando >= 1:
            print("Ainda faltam acertar {} letras".format(letras_faltando))
        else:
            pass

    if acertou:
        mensagem_vencedor()
    else:
        mensagem_perdedor(palavra_secreta)


def mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def começo():
    print("**" * 15)
    print("VAMOS JOGAR FORCA !?")
    print("**" * 15)


def mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if erros == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if erros == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if erros == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if erros == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def seleção_palavra():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def letras_que_faltam(letras_certas, palavra_secreta, chute):
    letras_faltando = int(letras_certas.count("_"))
    for LT in palavra_secreta:
        if chute.upper() == LT.upper():
            letras_faltando -= 1
    return letras_faltando


def pede_chute():
    chute = input("Qual a letra ?")
    # com a função strip elevai tirar todos os espaços ao redor da letra EXP: "  miranha  " = "miranha"
    chute = chute.strip().upper()
    return chute


def maraca_chute_certo(palavra_secreta, chute, letras_certas):
    posição = 0
    for letra in palavra_secreta:
        if chute.upper() == letra.upper():
            letras_certas[posição] = letra
        posição += 1


if __name__ == "__main__":
    jogar()
