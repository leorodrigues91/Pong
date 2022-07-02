# Clássico jogo de Pong em Python 3 para iniciantes
# By @leorodrigues91

import turtle
import winsound

janela = turtle.Screen()
janela.title("Pong by @leorodrigues91")
janela.bgcolor("black")
janela.setup(width=800, height=600)
janela.tracer(0)

# Pontuação
pontos_a = 0
pontos_b = 0

# Raquete A
raquete_a = turtle.Turtle()
raquete_a.speed(0)
raquete_a.shape("square")
raquete_a.color("white")
raquete_a.shapesize(stretch_wid=5, stretch_len=1)
raquete_a.penup()
raquete_a.goto(-350, 0)


# Raquete B
raquete_b = turtle.Turtle()
raquete_b.speed(0)
raquete_b.shape("square")
raquete_b.color("white")
raquete_b.shapesize(stretch_wid=5, stretch_len=1)
raquete_b.penup()
raquete_b.goto(350, 0)

# Bola
bola = turtle.Turtle()
bola.speed(0)
bola.shape("circle")
bola.color("white")
bola.penup()
bola.goto(0, 0)
bola_dx = 0.15
bola_dy = 0.15

# Placar
placar = turtle.Turtle()
placar.speed(0)
placar.color("white")
placar.penup()
placar.hideturtle()
placar.goto(0, 260)
placar.write(
    f"Jogador A: {pontos_a}     Jogador B: {pontos_b}",
    align="center",
    font=("Courier", 20, "normal")
    )

# Funções
def raquete_a_up():
    y = raquete_a.ycor()
    y += 20
    raquete_a.sety(y)

def raquete_a_down():
    y = raquete_a.ycor()
    y -= 20
    raquete_a.sety(y)

def raquete_b_up():
    y = raquete_b.ycor()
    y += 20
    raquete_b.sety(y)

def raquete_b_down():
    y = raquete_b.ycor()
    y -= 20
    raquete_b.sety(y)

# Comandos do teclado
janela.listen()
janela.onkeypress(raquete_a_up, "w")
janela.onkeypress(raquete_a_down, "s")
janela.onkeypress(raquete_b_up, "Up")
janela.onkeypress(raquete_b_down, "Down")



# Main game loop
while True:
    janela.update()

    # Movendo a bola
    bola.setx(bola.xcor() + bola_dx)
    bola.sety(bola.ycor() + bola_dy)

    # Colisão da bola com as bordas da tela
    if bola.ycor() > 290:
        bola.sety(290)
        bola_dy *= -1
        winsound.PlaySound("./Sound/bounce.wav", winsound.SND_ASYNC)
    
    if bola.ycor() < -280:
        bola.sety(-280)
        bola_dy *= -1
        winsound.PlaySound("./Sound/bounce.wav", winsound.SND_ASYNC)
    
    if bola.xcor() > 390:
        bola.goto(0, 0)
        bola_dx *= -1
        pontos_a += 1
        placar.clear()
        placar.write(
            f"Jogador A: {pontos_a}     Jogador B: {pontos_b}",
            align="center",
            font=("Courier", 20, "normal")
        )
    
    if bola.xcor() < -390:
        bola.goto(0, 0)
        bola_dx *= -1
        pontos_b += 1
        placar.clear()
        placar.write(
            f"Jogador A: {pontos_a}     Jogador B: {pontos_b}",
            align="center",
            font=("Courier", 20, "normal")
        )
    
    # Colisão da bola com as raquetes
    if bola.xcor() > 340 and (bola.ycor() < raquete_b.ycor() + 50 and bola.ycor() > raquete_b.ycor() - 50):
        bola.setx(340)
        bola_dx *= -1
        winsound.PlaySound("./Sound/bounce.wav", winsound.SND_ASYNC)
    
    if bola.xcor() < -340 and (bola.ycor() < raquete_a.ycor() + 50 and bola.ycor() > raquete_a.ycor() - 50):
        bola.setx(-340)
        bola_dx *= -1
        winsound.PlaySound("./Sound/bounce.wav", winsound.SND_ASYNC)
