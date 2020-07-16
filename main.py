from tkinter import *
root = Tk()
root.title("Simple Calculator")  # Title
root.resizable(0, 0)  # Remove maximize button

# Create entry field
e = Entry(root, width=32, font=('Arial', 15), borderwidth=2)
e.insert(0, str(0)+'.'+str(0))
e.grid(row=0, column=0, columnspan=4, pady=10)


# When a number is clicked
def click(number):
    current = e.get()
    e.delete(0, END)
    if current == '0.0':
        e.insert(0, str(number))
    else:
        e.insert(0, str(current) + str(number))


# Clear screen
def clc():
    e.delete(0, END)
    e.insert(0, str(0)+'.'+str(0))


# Add operator
def operate(symbol):
    current = e.get()
    if current[-1] in ['+', '-', '/', '*', '.']:
        return
    if symbol == '.':
        n = len(current)
        for i in range(n - 2, -1, -1):
            if current[i] in ['+', '-', '/', '*']:
                break
            elif current[i] == '.':
                return
    e.delete(0, END)
    e.insert(0, str(current) + symbol)


# Evaluate the expression
def evaluate():
    expression = e.get()
    if expression[-1] == '+' or expression[-1] == '-' or expression == '.':
        expression += '0'
    elif expression[-1] == '/' or expression[-1] == '*':
        expression += '1'
    e.delete(0, END)
    e.insert(0, float(eval(expression)))


# Create buttons
button1 = Button(root, text='1', padx=40, pady=20, command=lambda: click(1))
button2 = Button(root, text='2', padx=40, pady=20, command=lambda: click(2))
button3 = Button(root, text='3', padx=40, pady=20, command=lambda: click(3))
button4 = Button(root, text='4', padx=40, pady=20, command=lambda: click(4))
button5 = Button(root, text='5', padx=40, pady=20, command=lambda: click(5))
button6 = Button(root, text='6', padx=40, pady=20, command=lambda: click(6))
button7 = Button(root, text='7', padx=40, pady=20, command=lambda: click(7))
button8 = Button(root, text='8', padx=40, pady=20, command=lambda: click(8))
button9 = Button(root, text='9', padx=40, pady=20, command=lambda: click(9))
button0 = Button(root, text='0', padx=40, pady=20, command=lambda: click(0))

add = Button(root, text='+', padx=40, pady=20, command=lambda: operate('+'))
subtract = Button(root, text='-', padx=41, pady=20, command=lambda: operate('-'))
multiply = Button(root, text='x', padx=40, pady=20, command=lambda: operate('*'))
divide = Button(root, text='/', padx=41, pady=20, command=lambda: operate('/'))
decimal = Button(root, text='.', padx=41, pady=20, command=lambda: operate('.'))

equal = Button(root, text='=', padx=39, pady=20, command=lambda: evaluate())
clear = Button(root, text='C', padx=186, pady=20, command=lambda: clc())

# Put buttons on screen
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
button0.grid(row=4, column=1)

add.grid(row=1, column=3)
subtract.grid(row=2, column=3)
multiply.grid(row=3, column=3)
divide.grid(row=4, column=3)
decimal.grid(row=4, column=0)

equal.grid(row=4, column=2)
clear.grid(row=5, column=0, columnspan=4)

# Run main loop
root.mainloop()