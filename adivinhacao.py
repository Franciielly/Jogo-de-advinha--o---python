import random

# Função para gerar dicas com base no número tentado 
def gerar_dica (numeroT, numeroC):
    if numeroT > numeroC:
        print("Tente um número menor")
    elif numeroT < numeroC:
        print("Tente um número maior.")
    else:
        print("parabéns! Você acertou o número secreto!")

# Função principal do jogo
def jogoAdivinhacao():
    tentativa = 5 # número de tentiva
    numeroC = random.randint(1,100) # Gera número secreto

    print("-----------Jogo de adivinhação--------------")
    print("\n")
    print("Insira um número e tente descobrir o número secreto!")

    while tentativa > 0: # Loop que continua até o usuário ter tentativa
        numeroT = int(input("Digite um número: "))
        gerar_dica(numeroT,numeroC) # Fornece dica com base no número digitado

        if numeroT == numeroC: 
            break 

        tentativa -= 1 
        print(f"Número incorreto. Você ainda tem {tentativa} restante\n")

        if tentativa == 0 and numeroT != numeroC:
            print(f"Que pena! o número correto era {numeroC}")

# Inicia jogo
jogoAdivinhacao()

    
        
    