import turtle
colors = ["blue", "red", "yellow", "green"]
rad = 120
for i in range (len(colors)):
    turtle.pensize (0)
    turtle.pencolor (colors[i])
    turtle.fillcolor (colors[i])
    turtle.begin_fill ()
    turtle.circle (rad,180)
    turtle.seth (-90+270*i)
    turtle.fd (rad*2)
    turtle.end_fill ()
