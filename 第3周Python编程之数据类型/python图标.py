import turtle
 
def snakeBody(direction, color, bodySize):
 
    #画笔设置
    turtle.pensize(bodySize)
    turtle.pencolor(color)
 
    #尾巴
    turtle.seth(direction)
    turtle.fd(40)
 
    #第一转
    turtle.circle(-60, 90)
 
    #身体
    turtle.fd(135)
    turtle.seth(direction)
 
    #脖子
    turtle.fd(85)
    turtle.seth(direction + 90)
 
    #头
    turtle.fd(110)
 
    #眼睛
    turtle.pencolor("white")
    pythonsize = 20
    turtle.pensize(pythonsize)
    turtle.seth(- direction)
    turtle.circle(10, 360)

def main():
 
    direction = 90
    bodySize = 80
     
    turtle.up()
    turtle.setpos(-120,-40)
    turtle.down()
 
    snakeBody(direction, "blue", bodySize)
 
    turtle.up()
    turtle.setpos(160,75)
    turtle.down()
 
    snakeBody(-direction, "yellow", bodySize)
 
 
main()
