import turtle as t
rx=[]
ry=[]
move_cnt=0
t.pensize(20)
t.pencolor("red")

def fill_route():
    t.pendown()
    (a,b)=t.position()
    t.write(a,b)
    p=int((b-ry[0])//20)
    for i in range(0,p):
        t.goto(rx[0],b-20*2*i)
        t.goto(rx[0],b-20*(2*i+1))
        t.goto(a,b-20*(2*i+1))
        t.goto(a,b-20*(2*i+2))          
def clicked(x,y):
    global move_cnt
    move_cnt=move_cnt+1
    rx.append(x)
    ry.append(y)
def list_clear():
    global move_cnt
    del rx[1:move_cnt]
    del ry[1:move_cnt]
    move_cnt=1
def key_e():
    list_clear()
def key_d():
    fill_route()
t.setup(600,600)
s=t.Screen()
t.speed(1)
t.penup()
t.showturtle()
s.onkey(key_e,"e")
s.onkey(key_d,"d")
s.onscreenclick(clicked)
s.listen()
