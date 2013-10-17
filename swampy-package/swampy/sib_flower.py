# Flower excercise (4.2) from Week 0

# Name: Patrick Kennedy


from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()				



# This is where you put code to move bob

def petals (snapping, sides, theta):
	for i in range (2):
		arc2(snapping, sides, theta)
		lt(bob, 180)

def petunia (snapping, sides, radius, theta):
	for i in range (sides):
		petals(snapping, sides, theta)
		lt (snapping, float(360)/sides)

def movingday (snapping, length):
	pu(snapping)
	fd(snapping, length)
	pd(snapping)


#pasting in my code from polygon:

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

petunia(bob, 12, 10, 400)



wait_for_user()					

