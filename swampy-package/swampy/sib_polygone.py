#Excercise #2- use a function call and loop to draw a square

#Name: Patrick Kennedy

from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()		

#function to draw
def DrawASquare(squirtle, length):
	lt(squirtle)
 	fd(squirtle, length)

def Polygone(squirtle, length, degrees):
 	rt(squirtle, degrees)
 	fd(squirtle, length)

def Circle(squirtle, radius):
 	circ = 2 * 3.1459 * radius
 	n = (circ / 3) + 1
 	length = circ/n
 	Polygone(squirtle, radius, n)

def Arc(squirtle, radius, theta):
 	bob.delay = .01
 	length = 2 * 3.1459 * radius * theta / 360
 	n = int(length / 3) + 1
 	howfar = length / n
 	degree = float(theta) / n  #had to add 'float' for rounding to get all the way around
 	for i in range (n):
 		fd (bob, howfar)
 		lt (bob, degree)


#refactored functions code
def Polyline(hurtle, sides, length, theta):
	for i in range (sides):
		fd(bob, length)
		lt(bob, theta)

def polygon2(hurtle, sides, length):
	theta = float(360)/sides
	Polyline(hurtle, sides, length, theta)

def arc2(hurtle, radius, theta=360):
	arcHowfar = 2 * 3.1459 * radius * theta / 360
	sides = int(arcHowfar/3) + 1
	howfar = float(theta) / sides
	degree = float(theta) / sides
	Polyline(hurtle, sides, howfar, degree)

def circle2(hurtle, radius):
	arc2(hurtle, radius, 360)

bob.delay = .01
polygon2(bob, 4, 25) #testing on a square
circle2(bob, 5) #testing on a polygone
arc2(bob, 8, 270) #testing the arc





#old original calls, can be deleted later

# # #loop to draw a square
# for i in range (4):
# 	DrawASquare(bob, 100)

# pu(bob)
# fd(bob, 100)
# pd(bob)

# #stuff necessary to draw a polygone
# sides = 7
# degrees = (360/sides)

# #loop to draw a polygone

# for i in range(sides):
#  	Polygone(bob, 25, degrees)



# #to move bob into a new position away from the other drawings
# lt(bob, 220)
# pu(bob)
# fd(bob, 200)
# pd(bob)


# #loop to draw a circle
# #assuming a 100 sided polygone with a radius of 75
# bob.delay = .01

# for i in range(100): #went with 100 because it draws a full circle
# 	Circle(bob, 2) 

# #Note: I am unsure why the size of the circle grows with a smaller radius, as my forumula looks ok. 
# #With a decimal amount input the circle is roughly the same size as if I were using a radius in the 100s.

# pu(bob)
# fd(bob, 25)
# pd (bob)

# #now to play around with arc

# arc(bob, 30, 360)




wait_for_user()