import random

def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 11) # gerar número aleatório
    total_de_tentativas = 0
    pontos = 10 #número de pontos
    pontos_perdidos = 0

    print("Qual nivel de deficuldade?") 
    print("(1) Fácil, (2) Médio (3) Difícil")

    nivel = int(input("Digite o nivel desejado: ")) #necessário por int para entrar com inteiro e não uma str.

    if(nivel == 1):
        total_de_tentativas = 5
    elif(nivel == 2):
        total_de_tentativas = 3
    else:
        total_de_tentativas = 2


    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 10: ")
        print("Você digitou " , chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 10):
            print("Você deve digitar um número entre 1 e 10!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos!". format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior do que o número secreto.")
            elif(menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos 

    print("Fim do jogo, O número era",numero_secreto)

if(__name__ == "__main__"):
    jogar()
