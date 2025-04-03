from tkinter import *

window = Tk()
window.geometry("320x260")
window.title("Calculator")
window.resizable(False, False)

number = ""
history = []

def mainframe():
    global calculateframe
    
    calculateframe = Frame(window, width = 320, height = 260, bg = "teal")
    calculateframe.place(x = 0, y = 0)
    
mainframe()

def updatefield(value):
    global number
    number += str(value)
    input.config(state = "normal")
    input.delete(0, END)
    input.insert(0, number)
    input.config(state = "readonly")

def clearfield():
    global number
    number = ""
    input.config(state = "normal")
    input.delete(0, END)
    input.config(state = 'readonly')

def calculate():
    global number, history
    try:
        result = eval(number)
        history.append(f"{number} = {result}")
        number = str(result)
        input.config(state = "normal")
        input.delete(0, END)
        input.insert(0, number)
        input.config(state = "readonly")
        
    except Exception as e:
        input.config(state = "normal")
        input.delete(0, END)
        input.insert(0, "Error")
        input.config(state = "readonly")
        number = ""

def showhistory():
    historyframe = Frame(calculateframe, width = 320, height = 260, bg = "teal")
    historyframe.place(x = 0, y = 0)
    historyframe.pack_propagate(False)

    for calc in history:
        def usehistory(value = calc.split(" = ")[1]):
            #value.strip()
            updatefield(value)
            
        Button(historyframe, text = calc, command = usehistory, width = 30).pack(pady = 5)
        
    Button(historyframe, text = "Back", command = mainframe, width = 50).pack(anchor = "s")

input = Entry(calculateframe, font = ("Arial", 18), width = 20, state = 'readonly')
input.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)

#ai start
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('History', 5, 0)
]
#ai end

for btn_text, row, col in buttons:
    if btn_text == "=":
        Button(calculateframe, text = btn_text, width = 10, height = 2, command = calculate).grid(row = row, column = col)

    elif btn_text == "C":
        Button(calculateframe, text = btn_text, width = 10, height = 2, command = clearfield).grid(row = row, column = col)

    elif btn_text == "History":
        Button(calculateframe, text = btn_text, width = 30, height = 2, command = showhistory).grid(row = row, column = col, columnspan = 4)

#ai start
    else:
        Button(calculateframe, text = btn_text, width = 10, height = 2, command = lambda value = btn_text: updatefield(value)).grid(row = row, column = col)

#ai end
window.mainloop()