from tkinter import *
import time
#set variables
canvas_width = 800
canvas_height = 600
canvas_colour = "black"

p1_x = canvas_width/1.5
p1_y = canvas_height
p2_x = canvas_width/3
p2_y = canvas_height

p1_colour="green"
p2_colour="red"
line_width = 10
line_length = 10

#Functions

#Player controls
def p1_move_N(self):
    global p1_y
    canvas.create_line(p1_x, p1_y, p1_x, p1_y-line_length, width=line_width, fill=p1_colour)
    p1_y = p1_y - line_length
def p1_move_S(self):
    global p1_y
    canvas.create_line(p1_x, p1_y, p1_x, (p1_y+line_length), width=line_width, fill=p1_colour)
    p1_y = p1_y + line_length
def p1_move_E(self):
    global p1_x
    canvas.create_line(p1_x, p1_y, (p1_x+line_length), p1_y, width=line_width, fill=p1_colour)
    p1_x = p1_x + line_length
def p1_move_W(self):
    global p1_x
    canvas.create_line(p1_x, p1_y, (p1_x-line_length), p1_y, width=line_width, fill=p1_colour)
    p1_x = p1_x - line_length
    
def p2_move_N(self):
    global p2_y   
    canvas.create_line(p2_x, p2_y, p2_x, p2_y-10, width=line_width, fill=p2_colour) 
    p2_y = p2_y - 10

def p2_move_S(self):
    global p2_y
    canvas.create_line(p2_x, p2_y, p2_x, (p2_y+line_length), width=line_width, fill=p2_colour)
    p2_y = p2_y + line_length
def p2_move_E(self):
    global p2_x
    canvas.create_line(p2_x, p2_y, (p2_x+line_length), p2_y, width=line_width, fill=p2_colour)
    p2_x = p2_x + line_length
def p2_move_W(self):
    global p2_x
    canvas.create_line(p2_x, p2_y, (p2_x-line_length), p2_y, width=line_width, fill=p2_colour)
    p2_x = p2_x - line_length
    
    
def erase_all(self):
    canvas.delete(ALL)
#Main

window = Tk()
window.title("Iskechtalittle")
canvas = Canvas(bg=canvas_colour, width=canvas_width, height=canvas_height, highlightthickness=0)


#bind movememnt to key presses
window.bind("<Up>", p1_move_N)
window.bind("<Down>", p1_move_S)
window.bind("<Right>", p1_move_E)
window.bind("<Left>", p1_move_W)

window.bind("w", p2_move_N)
window.bind("s", p2_move_S)
window.bind("d", p2_move_E)
window.bind("a", p2_move_W)
window.bind("u", erase_all)
canvas.pack()
window.after(2000, p2_move_N)
window.mainloop()