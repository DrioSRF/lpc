import turtle
import random

# Criando a tartaruga do jogador 1
player_one = turtle.Turtle()
player_one.color("green")
player_one.shape("turtle")
player_one.penup()
player_one.goto(-200,100)

# Criando a tartaruga do jogador 2
player_two = player_one.clone()
player_two.color("blue")
player_two.penup()
player_two.goto(-200,-100)

# Criando a chegada para a tartaruga do jogador 1
player_one.goto(300,60)
player_one.pendown()
player_one.circle(40)
player_one.penup()
player_one.goto(-200,100)

# Criando a chegada para a tartaruga do jogador 2
player_two.goto(300,-140)
player_two.pendown()
player_two.circle(40)
player_two.penup()
player_two.goto(-200,-100)

# Começando o jogo
for i in range(20):

    # Rolando o dado para o jogador 1
    player_one_turn = input("Jogador 1: aperte 'Enter' para rolar o dado")
    die_outcome = random.choice([1,2,3,4,5,6])

    # Mostrando o resultado da rolagem do jogador 1
    print("A rolagem do dado foi: ")
    print(die_outcome)

    # Mostrando a quantidade de espaços que a tartaruga do jogador 1 irá
    # andar
    print("O número de passos será")
    print(20*die_outcome)

    # Verificando se o jogador 1 estrá na posição de vitória com essa rolagem
    if ((player_one.pos()[0] + 20*die_outcome) >= 300):

        player_one.goto(300,100)
        print("Vitória do Jogador 1!")
        break
        
    # Fazendo a tartaruga do jogador 1 andar a determinada quantidade de
    # espaços rolados no dado 20 vezes
    else:

        player_one.forward(20*die_outcome)
        
    # Rolando o dado para o jogador 2
    player_two_turn = input("Jogador 2: aperte 'Enter' para rolar o dado")
    die_outcome = random.choice([1,2,3,4,5,6])

    # Mostrando o resultado da rolagem do jogador 2
    print("A rolagem do dado foi: ")
    print(die_outcome)

    # Mostrando a quantidade de espaços que a tartaruga do jogador 2 irá
    # andar
    print("O número de passos será")
    print(20*die_outcome)

        
    # Verificando se o jogador 2 estrá na posição de vitória com essa rolagem
    if ((player_two.pos()[0] + 20*die_outcome) >= 300):

        player_two.goto(300,-100)
        print("Vitória do Jogador 2!")
        break

    # Fazendo a tartaruga do jogador 2 andar a determinada quantidade de
    # espaços rolados no dado 20 vezes
    else:
        
        player_two.forward(20*die_outcome)

turtle.done()
