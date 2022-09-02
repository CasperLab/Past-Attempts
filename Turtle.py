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

alex_win = False

alex.up()
bob.up()
alex.shape("turtle")
bob.shape("turtle")
alex.color("blue")
bob.color("red")

alex.speed(2)
bob.speed(2)

alex.goto(0,-100)
bob.goto(-30,-100)
alex.left(90)
bob.left(90)

while True:
    alex_distance = r.randrange(1,21)
    bob_distance = r.randrange(1,21)
    
    alex.forward(alex_distance)
    print(alex_distance)
    bob.forward(bob_distance)
    print(bob_distance)
    
    
    if bob_distance - alex_distance > 10:
        bob_wincount += 1
        print("Bob wins: " + str(bob_wincount) + ", " + "Alex wins: " + str(alex_wincount))
        alex.goto(0,-100)
        bob.goto(-30,-100)
    elif alex_distance - bob_distance > 10:
        alex_wincount += 1
        print("Bob wins: " + str(bob_wincount) + ", " + "Alex wins: " + str(alex_wincount))    
    else:
        print("Still racing")
     
    if alex_wincount == 10:
        print("Alex is the winner!")
        break
    elif bob_wincount == 10:
        print("Bob is the winner!")
        break
    else:
        None
        
wn.exitonclick()