from tkinter import *


canvas_width = 1200
canvas_height = 800
canvas_colour = "blue"

p1_x = canvas_width/2
p1_y = canvas_height

p1_colour="white"
p2_colour="black"
line_width = 20
line_length = 20

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
    
    
def erase_all(self):
    canvas.delete(ALL)

window = Tk()
window.title("SketchGameOmonov")
canvas = Canvas(bg=canvas_colour, width=canvas_width, height=canvas_height, highlightthickness=0)


#bind movememnt to key presses
window.bind("<Up>", p1_move_N)
window.bind("<Down>", p1_move_S)
window.bind("<Right>", p1_move_E)
window.bind("<Left>", p1_move_W)
window.bind("u", erase_all)
canvas.pack()
window.mainloop()