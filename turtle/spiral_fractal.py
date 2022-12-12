import turtle
import math

# Entrada que irá decidir o número de termos de Fibonacci
n = int(input("Número de termos (o valor precisa ser > 1): "))

# Desenhando a espiral fractal de Fibonacci e mostrando o termo
# correspondente da sequência de Fibonacci

print("Série de Fibonacci para", n, "elementos :")

#Inicializando as variáveis que representarão a sequência de fibonacci e
# a variável que será a tartaruga
minus1 = 0
minus2 = 1
pencil = turtle.Turtle()
pencil.speed(100)

# Primeiro quadrado
pencil.forward(minus2*10)
pencil.left(90)
pencil.forward(minus2*10)
pencil.left(90)
pencil.forward(minus2*10)
pencil.left(90)
pencil.forward(minus2*10)

# Seguindo com a sequência de fibonacci.
aux = minus1
minus1 = minus2
minus2 = aux + minus2

# Desenhando os outros quadrados
for i in range(1, n):

    pencil.backward(minus1*10)
    pencil.right(90)
    pencil.forward(minus2*10)
    pencil.left(90)
    pencil.forward(minus2*10)
    pencil.left(90)
    pencil.forward(minus2*10)
        
    # Seguindo com a sequência de fibonacci.
    aux = minus1
    minus1 = minus2
    minus2 = aux + minus2

# Trazendo a tartaruga para o centro da espiral
pencil.penup()
pencil.setposition(10, 0)
pencil.seth(0)
pencil.pendown()

# Mudando a cor do rastro da tartaruga para verde
pencil.pencolor("green")

# Desenhando a espiral dentro dos quadrados
pencil.left(90)
minus1 = 0
minus2 = 1

for i in range(n):

    print(minus2)
    spiral = math.pi*minus2 * 10/2
    spiral /= 90

    for j in range(90):

        pencil.forward(spiral)
        pencil.left(1)

    # Seguindo com a sequência de fibonacci.
    aux = minus1
    minus1 = minus2
    minus2 = aux + minus2

turtle.done()
