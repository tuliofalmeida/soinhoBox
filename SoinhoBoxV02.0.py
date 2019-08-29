from random import randint
import random

print("Bem-vindo a Caixa Comportamental \nO objetivo da caixa e treinar o animal")
inicio = input("O sagui esta habituado? (Digite s/n): ")
if(inicio == "s"):
    print("Otimo, com o sagui habituado podemos comecar!")
    habituado = True
    aprox = False
    som = False
    testeFinal = False
    numAprox = 0
    Lista = ["Direita", "Esquerda"]
    Opcao = ["Som 1", "Som 2"]
    acerto = 0
    erros = 0
    print("O sagui precisa se aproximar do sensor 20x, com uma distancia < que 30cm")
    while(aprox == False):
        varDis = randint(0, 60)  
        if(varDis <30):
            numAprox += 1
            print("O sagui conseguiu",varDis, "cm por", numAprox ,"vezes")
            print("Sagui conquistou 0,5 ml de recompensa")
        if(numAprox == 20):
            aprox = True
            print("O sagui esta pronto para a proxima fase")
    print("Vamos iniciar a Fase 2\nMétodo de discriminação de estímulos auditivos\npara primatas através do condicionamento operante.")
    print("Serao emitidos 2 sons, o 'Som 1' e o 'Som 2',\nQuando for emitido o 'Som 1' o sagui deve encostar na barra da esquerda\nQuando for emitido o 'Som 2' o sagui deve encostar na barra da direita")
    while(som == False):
        varSom = random.choice(Lista)
        print("O 'Som 1' foi emitido o sangui encostou na barra da esquerda? ")
        print(varSom)
        if (varSom == "Esquerda"):
            print("O sagui acertou, vamos continuar!")
            varSom = random.choice(Lista)
            print("O 'Som 2' foi emitido o sangui encostou na barra da direita? ")
            print(varSom)
            if(varSom == "Direita"):
                trocaFase = input("Podemos iniciar a proxima fase?(Digite s/n)")
                if(trocaFase == "s"):
                    som = True
                else:
                    som = False
            else:
                som = False
        else:
            som = False
    print("Exercicio final para habituacao do sagui\nEm 30 minutos o sagui deve conseguir realizar o teste 50x")
    while(testeFinal == False):
        print("O sagui possui", acerto, "acertos", "e", erros, "erros")
        varSom = random.choice(Lista)
        varOpcao = random.choice(Opcao)
        print("O", varOpcao , "foi emitido o sagui encostou na barra da", varSom, "? ")
        print("O sagui encontou na barra da ",varSom)
        if (varSom == "Esquerda" and varOpcao == "Som 1"):
            print("O sagui acertou!")
            acerto += 1
        if (varSom == "Direita" and varOpcao == "Som 2"):
            print("O sagui acertou!")
            acerto += 1
        if (varSom == "Esquerda" and varOpcao == "Som 2"):
            print("O sagui errou!")
            erros += 1
        if (varSom == "Direita" and varOpcao == "Som 1"):
            print("O sagui errou!")
            erros += 1
        if(acerto == 50):
            print("O sagui conseguiu passar no teste!")
            testeFinal = True
        elif(erros == 50):
            print("O sagui falhouno teste!")
            break
        else:
            testeFinal = False
    if(testeFinal == True):
        print("Seu sagui esta conseguindo discriminar os sons!")
else:
    print("Habitue o sagui primeiro")
