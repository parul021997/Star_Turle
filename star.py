import turtle as t
import random as r
rock=t.Turtle()

win=t.getscreen()
win.bgcolor("black")
rock.color("yellow")
rock.speed(0)
for i in range(50):
    x=r.randint(-400,400)
    y=r.randint(-400,400)
    rock.up()
    rock.goto(x,y)
    
    rock.down()
    for i in range(5):
        rock.fd(20)
        rock.lt(144)
