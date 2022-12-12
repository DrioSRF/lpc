import turtle

scr=turtle.Screen()

# Criando a tartaruga "ttle"
ttle=turtle.Turtle()


def make_triangle(x, y):

    # Levantando a "caneta" do papel
    ttle.penup()

    # Movendo o a tartaruga para a posição (x, y)
    ttle.goto(x, y)

    # Colocando a "caneta" no papel
    ttle.pendown()

    for i in range(3):

        # Movendo a "caneta" para frente 100 unidades
        ttle.forward(100)

        # Girando a direção da "caneta" 120 graus anti-horário
        ttle.left(120)

        # Movendo a "caneta" para frente 100 unidades
        ttle.forward(100)

# Função especial que faz com que a função "make_triangle" receba a posição
# na tela onde o botão direito do mouse foi clicado e desenha um triângulo
# nessa posição
turtle.onscreenclick(make_triangle,1)

turtle.listen()

turtle.done()
