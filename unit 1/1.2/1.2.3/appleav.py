import turtle
import random

apple_image = "apple.gif"
pear_image = "pear.gif"

wn = turtle.Screen()
wn.setup(width=607, height=406)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.addshape(pear_image)
wn.bgpic("background.gif")

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

class Apple(turtle.Turtle):
	def __init__(self, shape = "apple_image"):
		super().__init__(shape)
		self.penup()
		self.speed(0.6)
		