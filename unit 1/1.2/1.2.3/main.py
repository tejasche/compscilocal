#   a123_apple_1.py
import turtle as trtl
import random as rand

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
pear_image = "pear.gif"

wn = trtl.Screen()
wn.setup(width=607, height=406)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.addshape(pear_image)
wn.bgpic("background.gif")

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

apple = trtl.Turtle()
text = trtl.Turtle()

text.penup()
text.hideturtle()
apple.penup()
apple.speed(0.6)
#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def drawapple(active_apple):
	active_apple.shape(pear_image)
	wn.update()

def falling():
	text.clear()
	apple.goto(apple.xcor(), apple.ycor() - 300)

def drawtext(input):
	text.goto(apple.xcor() - 23, apple.ycor() - 45)
	text.write(input, font = ("Arial", 55, "normal"))

def newlocation(turt):
	if len(letters) > 0:
		turt.goto(rand.randint(-200, 200), rand.randint(-200, 200))

def newletter():
	return letters.pop(rand.randint(0, len(letters) - 1))

def newturtle(apple):
	apple.shape(apple_image)
	drawtext(newletter())
	wn.update()

	for i in range(0, len(letters)):
 
#-----function calls-----
drawapple(apple)
drawtext("A")

wn.onkeypress(falling, "a")

wn.listen()
wn.mainloop()