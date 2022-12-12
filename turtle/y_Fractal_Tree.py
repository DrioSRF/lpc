import turtle

pencil = turtle.Turtle()
pencil.speed('fastest')

# Mudando a orientação da tartaruga para cima
pencil.left(90)

# O ângulo entre a base e os galhos do Y
angle = 30

# Função para plotar o Y
def do_Y(size, level):

    if level > 0:
        turtle.colormode(255)

        # Mudando a cor dos galhos de acordo com o nível
        pencil.pencolor(255//level, 140//level, 0)

        # Base da árvore
        pencil.forward(size)

        pencil.right(angle)

        # Chamada recursiva para a subarvore de direita
        do_Y(0.8 * size, level-1)

        pencil.pencolor(255//level, 140//level, 0)

        pencil.left( 2 * angle )

        # Chamada recursiva para a subarvore de esquerda
        do_Y(0.8 * size, level-1)

        # Mudando a cor dos galhos de acordo com o nível
        pencil.pencolor(255//level, 140//level, 0)

        pencil.right(angle)
        pencil.backward(size)


# Árvore de tamanho e nível determinados pela entrada
size = int(input("Escala da árvore (valor > 0): "))
level = int(input("Número de níveis em um galho (valor > 0): "))

# Chamada para a função que plota a árvora de Y
do_Y(size, level)

turtle.done()
