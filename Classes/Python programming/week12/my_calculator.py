from tkinter import *
from decimal import *


def click(key):
    if key == "=":
        try:
            result = str(eval(display.get()))[0:10]
            display.insert(END, " = " + result)
        except:
            display.insert(END, " --> Error!")
    elif key == "C":
        display.delete(0, END)
    elif key == constants_list[0]:
        display.insert(END, "3.141592654")
    elif key == constants_list[0]:
        display.insert(END, "3.141592654")
    elif key == constants_list[1]:
        display.insert(END, "300000000")
    elif key == constants_list[2]:
        display.insert(END, "330")
    elif key == constants_list[3]:
        display.insert(END, "149597887.5")
    else:
        display.insert(END, key)
        
def my_function(x="default text"):
    print(x)
    
def factorial(n):
    return "factorial (!)"

def to_roman(n):
    return "-> roman"

def to_binary(n):
    return "-> binary"

def square(n):
    return n**2

def from_binary(n):
    return "binary -> 10"

def square_root(n):
    return n**0.5

window = Tk()
window.title("MyCalculator_PETER")

top_row = Frame(window)
top_row.grid(row=0, column=0, columnspan=2, sticky=N)

display = Entry(top_row, width=45, bg="light blue")
display.grid()

num_pad = Frame(window)
num_pad.grid(row=1, column=0, sticky=W)

constants = Frame(window)
constants.grid(row=3, column=0, sticky=W)
constants_list = [
'pi',
'speed of light (m/s)',
'speed of sound (m/s)',
'ave dist to sun (km)' ]

r = 0
c = 0

for btn_text in constants_list:
    def cmd(x=btn_text):
        click(x)
    Button(constants, text=btn_text, width=22, command=cmd).grid(row=r, column=c)
r = r+1


functions = Frame(window)
functions.grid(row=3, column=1, sticky=E)
functions_list = [
'factorial (!)',
'-> roman',
'-> binary',
'binary -> 10' ]

r = 0
c = 0

for b in functions_list:
    def cmd(x=b):
        click(x)
    Button(functions, text=b, width=13, command=cmd).grid(row=r, column=c)
    r = r+1

num_pad_list = [
'7', '8', '9',
'4', '5', '6',
'1', '2', '3',
'0', '.', '=' ]

r = 0
c = 0 
r = 0
c = 0
for btn_text in num_pad_list:
    def cmd(x=btn_text):
        click(x)
        Button(num_pad, text=btn_text, width=5, command=cmd).grid(row=r,column=c)
        c = c+1
        if c > 2:
            c = 0
            r = r+1
            


operator = Frame(window)
operator.grid(row=1, column=1, sticky=E)
operator_list = [
'*', '/',
'+', '-',
'(', ')',
'C' ]

r = 0
c = 0
for btn_text in operator_list:
    Button(operator, text=btn_text, width=5,
               command=click).grid(row=r,column=c)
    c = c+1
    if c > 1:
        c = 0
        r = r+1

window.mainloop()
