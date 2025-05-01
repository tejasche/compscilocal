from tkinter import *

# ask the user for the theme
theme = input("Choose theme (dark or light): ").strip().lower()

# initialize the window
window = Tk()
window.geometry("320x255")  # set window size
window.title("Calculator")  # set window title
window.resizable(False, False)  # disable resizing

number = ""  # stores the current input number
history = []  # stores the calculation history

# define the button layout for the calculator
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('Delete', 5, 0),
    ('History', 5, 1)
]

# create main calculator frame
calculateframe = Frame(window, width = 320, height = 255)
calculateframe.place(x = 0, y = 0)

# function to initialize the main calculator frame
def mainframe(theme):
    global inputentry
    # create the input entry field
    inputentry = Entry(calculateframe, font = ("Arial", 18), width = 20, state = 'readonly')
    inputentry.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)

    # apply the selected theme
    if theme == "dark":
        window.config(bg = "black")
        inputentry.config(bg = "gray", fg = "black")
        calculateframe.config(bg = "black")
        btcolor = "black"
        textcolor = "white"

    else:
        window.config(bg = "white")
        inputentry.config(bg = "white", fg = "black")
        calculateframe.config(bg = "white")
        btcolor = "lightgray"
        textcolor = "black"

    # create buttons for the calculator by iterating through the button layout list
    for btntext, row, col in buttons:
        if btntext == "=":
            Button(calculateframe, text = btntext, width = 10, height = 2, bg = btcolor, fg = textcolor, command = calculate).grid(row = row, column = col)

        elif btntext == "C":
            Button(calculateframe, text = btntext, width = 10, height = 2, bg = btcolor, fg = textcolor, command = clearfield).grid(row = row, column = col)

        elif btntext == "History":
            Button(calculateframe, text = btntext, width = 30, height = 2, bg = btcolor, fg = textcolor, command = showhistory).grid(row = row, column = col, columnspan = 4)
            
        elif btntext == "Delete":
            Button(calculateframe, text = btntext, width = 10, height = 2, bg = btcolor, fg = textcolor, command = delete).grid(row = row, column = col)

        else:
            Button(calculateframe, text = btntext, width = 10, height = 2, bg = btcolor, fg = textcolor, command = lambda value = btntext: updatefield(value)).grid(row = row, column = col) # for rest of the numbers

#function to update the input field with the pressed button       
def updatefield(value):
    global number
    number += str(value) 
    inputentry.config(state = "normal")
    inputentry.delete(0, END)
    inputentry.insert(0, number)
    inputentry.config(state = "readonly")

# function to clear the input field
def clearfield():
    global number
    number = ""
    inputentry.config(state = "normal")
    inputentry.delete(0, END)
    inputentry.config(state = 'readonly')
    
#function to delete the last thing in the input field
def delete():
    global number
    number = number[:-1]
    inputentry.config(state="normal")
    inputentry.delete(0, END)
    inputentry.insert(0, number)
    inputentry.config(state="readonly")
    
# function to perform the calculation
def calculate():
    global number, history
    try:
        result = eval(number)
        history.append(f"{number} = {result}")
        number = str(result)
        inputentry.config(state = "normal")
        inputentry.delete(0, END)
        inputentry.insert(0, number)
        inputentry.config(state = "readonly")

    except Exception as e:
        inputentry.config(state = "normal")
        inputentry.delete(0, END)
        inputentry.insert(0, "Error")
        inputentry.config(state = "readonly")
        number = ""

# function to clear the history
def clearhistory():
    global history, historyframe, number
    history = []
    historyframe.destroy()

    calculateframe.tkraise()
    inputentry.config(state="normal")
    number = ""
    inputentry.delete(0, END)
    inputentry.insert(0, "History Cleared")
    inputentry.config(state="readonly")

# function to show the calculation history frame
def showhistory():
    global historyframe
    historyframe = Frame(calculateframe, width = 320, height = 255, bg = calculateframe.cget("bg"))
    historyframe.place(x = 0, y = 0)
    historyframe.pack_propagate(False)

    bgcolor = calculateframe.cget("bg")
    if bgcolor == "black":
        btcolor = "black"
        textcolor = "white"
    else:
        btcolor = "lightgray"
        textcolor = "black"

    # creates a button for each calculation in the history
    for calc in history:
        def usehistory(value = calc.split(" = ")[1]):
            updatefield(value)
            historyframe.destroy()
            calculateframe.tkraise()

        Button(historyframe, text = calc, command = usehistory, width = 30, bg = btcolor, fg = textcolor).pack(pady = 5)

    Button(historyframe, text = "Back", command = lambda: [historyframe.destroy(), calculateframe.tkraise()], width = 50, bg = btcolor, fg = textcolor).pack(anchor = "n")
    Button(historyframe, text = "Clear History", command = clearhistory, width = 50, bg = btcolor, fg = textcolor).pack(anchor = "s")

mainframe(theme)
window.mainloop()