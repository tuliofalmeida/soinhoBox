import sys
from random import randint
print("Bem-vindo ao Soinho Green Hill - Stage 1-1")  # Bem-vindo
# Input para saber se o soinho esta habituado
inicio = input("O soinho esta habituado? (Digite s/n) ")
fase2 = False
fase3 = False
som1 = ""
som2 = ""
if(inicio == "s"):  # Se estiver habituado deve armazenar isso em umma variavel e "funcionar" o sensor
    habituado = True  # se estiver habituado essa variavel se torna verdadeira
    # float(input("Distancia do sensor: ")) #variavel que detecta a distancia do sensor
    varDis = randint(0, 30)
    print("Distancia do sensor: ", varDis, "cm")
    if(varDis < 30):  # se a distancia do sensor for menor que 30, liberar agua. Se nao for nao tem recompensa
        print("O soinho ganhou 0,5ml de suco ")
        # float(input("Quantas vezes ele aproximou do sensor? ")) #se ele aproximar do sensor 20x ele aprendeu, se nao deve melhorar
        varRep = randint(20, 100)
        print("Quantas vezes ele aproximou do sensor? ", varRep)
        if(varRep > 20):
            print("Seu soinho passsou para fase 1-2!")
            fase2 = True  # se ele aproximou do sensor 20x ele passa de fase
        else:
            print("Precisa treinar melhor seu soinho")
    else:
        print("Sem recompensa pro soinho ")

    if(fase2 == True):
        print("Bem-vindo a Soinho's Green Hill 1-2")
        print("O soinho esta em um ambiente em que ele deve escutar o Som1.mp3 e tocar a barra da esquerda")
        som1 = input("O soinho conseguiu ouvir o Som1.mp3 e tocar na barra da equerda? (Digite s/n)")
    if(som1 == "s"):
        print("O soinho ganhou 0,5 ml de suco")
        print("O soinho deve ouvir o Som2.mp3 ele deve tocar na barra da direita")
        som2 = input(
            "O soinho conseguiu ouvir o Som2.mp3 e tocar na barra da direita? (Digite s/n)")
        if(som2 == "s"):
            print("O soinho ganhou 0,5 ml de suco e esta preparado para o desafio final")
            finalboss = input("Voce aceita o desafio? (Digite s/n)")
            if(finalboss == "s"):
                print("O soinho tem 30 minutos para tocar na barra 50 vezes! Ele tem 3 chances!")
                print("Tentativa 1: ")
                boss = True
                if(boss == True):
                    firstTry = randint(0, 70)
                    print("O soinho conseguiu ", firstTry, "vezes")
                    if(firstTry >= 50):
                        print("O soinho conseguiu completar o desafio")
                        fase3 = True
                    elif(firstTry<50):
                        print("O soinho nao conseguiu vamos para a Tentativa 2: ")
                        secondTry = randint(0, 85)
                        print("O soinho conseguiu ", secondTry, "vezes")
                        if(secondTry >= 50):
                            print("O soinho conseguiu passar proxima fase")
                            fase3 = True
                        elif(secondTry<50):
                            print("O soinho nao conseguiu vamos para a Tentativa 3: ")
                            thirdTry = randint(0,100)
                            print("O soinho conseguiu ", thirdTry, "vezes")
                            if(thirdTry > 50):
                                fase3 = True
                            else:
                                print("Melhor desistir desse soinho. Reinicie o processo")
                    else:
                        print("O soinho quase conseguiu chegar ao final boss")
            else:
                print("Voce e seu soinnho sao fracos")
        else:
            print("Seu soinho falhou no aprendizado")

    else:
        print("O soinho nao conseguiu aprender")
else:
    print("O soinho deve treinar mais")
if(fase3 == True):
    print("Bem-Vindo a Green Hill 1-3 - Voce tera que aguardar! infelizmente a fase ainda esta em contrucao")
