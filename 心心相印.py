# 心心相印
from turtle import *
  
setup(600,400,200,0)
bgcolor("lightgray")
  
def set_pos(x):
    penup()
    setpos(-50+x*120,-80)
    pendown()
      
def draw_heart():
    color('pink',"red")
    begin_fill()
    left(142)
    forward(111)
    circle(-70,180)
    left(77)
    circle(-70,180)
    forward(111)
    end_fill()
  
def main():
    for i in range(2):
        set_pos(i)
        draw_heart()
        left(142)
          
main()
hideturtle()
done()
