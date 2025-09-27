from turtle import Turtle, Screen
moha=Turtle()
moha.speed("fast")
moha.pensize(5)
window=Screen()
window.setup(1366,768)
while True:
    inp=window.textinput("لحضة من فضلك","ما الذي تريد أن ترسمه؟ دائرة.مربع.مثلث")
    if inp=="دائرة" or inp=="circle":
        moha.shape("turtle")
        moha.color("black")
        moha.circle(100)
        
        
    elif inp=="مربع" or inp== "square":
        moha.shape("square")
        moha.color("red")
        moha.pensize(10)
        for _ in range(4):
            moha.forward(200)
            moha.left(90)
    elif inp=="مثلث" or inp == "triangle":
        moha.color("brown")
        moha.shape("circle")
        moha.pensize(15)
        for _ in range(3):
            moha.forward(200)
            moha.left(120)
    elif inp=="خروج" or inp.lower()=="exit":
        break
#Finesh
moha.clear()
window.bgcolor("blue")
moha.teleport(0,0)
moha.write("Press any key" \
" To Exit..",font=("arial",22,"italic"),)
moha.teleport(0,-150)
moha.write("إضغط تاب للخروج",font=("arial",18,"normal"))




window.exitonclick()