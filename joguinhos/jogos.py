import forca
import adiviha

def escolhe_jogo():
    print("**" * 20)
    print("***********ESCOLHA UM JOGO!!************")
    print("**" * 20)

    print("adivinhação (1), Forca(2)")
    jogo = int(input("E então qual vai ser"))

    if jogo == 1:
        print("jogando Adivinhação")
        adiviha.jogar()
    elif jogo == 2:
        print("jogando Forca")
        forca.jogar()


if __name__ == "__main__":
    escolhe_jogo()