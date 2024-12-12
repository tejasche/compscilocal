#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
pear_image = "pear.gif"

wn = trtl.Screen()
wn.setup(width=607, height=406)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.addshape(pear_image)
wn.bgpic("background.gif")

apple = trtl.Turtle()
text = trtl.Turtle()

text.penup()
text.hideturtle()
apple.penup()
apple.speed(1)
#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def drawapple(active_apple):
  active_apple.shape(pear_image)
  wn.update()

def falling():
  apple.goto(apple.xcor(), apple.ycor() - 300)
  
def drawtext(input):
  text.goto(apple.xcor() - 23, apple.ycor() - 45)
  text.write(input, font = ("Arial", 55, "normal"))

#-----function calls-----
drawapple(apple)
drawtext("A")

if wn.onkeypress(falling, "a"):
  text.clear()

wn.listen()
wn.mainloop()