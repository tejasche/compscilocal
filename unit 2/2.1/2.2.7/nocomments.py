from tkinter import *

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

calculateframe = Frame(window, width = 320, height = 255, bg = "teal")
calculateframe.place(x = 0, y = 0)

def mainframe():
    global inputentry
    inputentry = Entry(calculateframe, font = ("Arial", 18), width = 20, state = 'readonly')
    inputentry.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)

    for btn_text, row, col in buttons:
        if btn_text == "=":
            Button(calculateframe, text = btn_text, width = 10, height = 2, command = calculate).grid(row = row, column = col)

        elif btn_text == "C":
            Button(calculateframe, text = btn_text, width = 10, height = 2, command = clearfield).grid(row = row, column = col)

        elif btn_text == "History":
            Button(calculateframe, text = btn_text, width = 30, height = 2, command = showhistory).grid(row = row, column = col, columnspan = 4)
            
        elif btn_text == "Delete":
            Button(calculateframe, text = btn_text, width = 10, height = 2, command = delete).grid(row = row, column = col)

        else:
            Button(calculateframe, text = btn_text, width = 10, height = 2, command = lambda value = btn_text: updatefield(value)).grid(row = row, column = col)
            
            
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
    historyframe = Frame(calculateframe, width = 320, height = 255, bg = "teal")
    historyframe.place(x = 0, y = 0)
    historyframe.pack_propagate(False)

    for calc in history:
        def usehistory(value = calc.split(" = ")[1]):
            updatefield(value)
            historyframe.destroy()
            calculateframe.tkraise()

        Button(historyframe, text = calc, command = usehistory, width = 30).pack(pady = 5)

    Button(historyframe, text = "Back", command = lambda: [historyframe.destroy(), calculateframe.tkraise()], width = 50).pack(anchor = "n")
    Button(historyframe, text = "Clear History", command = clearhistory, width = 50).pack(anchor = "s")

mainframe()
window.mainloop()