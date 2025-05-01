from tkinter import *

theme = input("Choose theme (dark or light): ").strip().lower()

window = Tk()
window.geometry("320x255")
window.title("Calculator")
window.resizable(False, False)

number = ""
history = []

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('Delete', 5, 0),
    ('History', 5, 1)
]

calculateframe = Frame(window, width = 320, height = 255)
calculateframe.place(x = 0, y = 0)

def mainframe(theme):
    global inputentry
    inputentry = Entry(calculateframe, font = ("Arial", 18), width = 20, state = 'readonly')
    inputentry.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)

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
    
def updatefield(value):
    global number
    number += str(value) 
    inputentry.config(state = "normal")
    inputentry.delete(0, END)
    inputentry.insert(0, number)
    inputentry.config(state = "readonly")

def clearfield():
    global number
    number = ""
    inputentry.config(state = "normal")
    inputentry.delete(0, END)
    inputentry.config(state = 'readonly')

def delete():
    global number
    number = number[:-1]
    inputentry.config(state="normal")
    inputentry.delete(0, END)
    inputentry.insert(0, number)
    inputentry.config(state="readonly")
    
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