import turtle as t
import random as r

wn = t.Screen()

alex = t.Turtle()
bob = t.Turtle()

total_distance = 0
distance = 0
angle = 0

alex_wincount = 0
bob_wincount = 0

alex.up()
bob.up()
alex.shape("turtle")
bob.shape("turtle")
alex.color("blue")
bob.color("red")

alex.speed(5)
bob.speed(5)

alex.goto(0,-100)
bob.goto(-30,-100)
alex.left(90)
bob.left(90)

while True:
    alex_distance = r.randrange(1,6)
    bob_distance = r.randrange(1,6)
    
    alex.forward(alex_distance)
    bob.forward(bob_distance)
      
    
    if bob.distance(-30,-100) > 120.0:
        bob_wincount += 1
        print("Bob wins: " + str(bob_wincount) + ", " + "Alex wins: " + str(alex_wincount))
        alex.goto(0,-100)
        bob.goto(-30,-100)
    elif alex.distance(0,-100) > 120.0:
        alex_wincount += 1
        print("Bob wins: " + str(bob_wincount) + ", " + "Alex wins: " + str(alex_wincount))  
        alex.goto(0,-100)
        bob.goto(-30,-100)
    else:
        None
     
    if alex_wincount == 10:
        print("Alex is the winner!")
        break
    elif bob_wincount == 10:
        print("Bob is the winner!")
        break
    else:
        None
        
wn.exitonclick()
