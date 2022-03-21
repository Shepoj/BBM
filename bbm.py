from tkinter import *
from time import *
window = Tk()
canvas = Canvas(window, width=1280, height=720)
canvas.pack()
a = (0, 50), (50, 100) # coordinates of the rectangle
rect = canvas.create_rectangle(a, fill="red")
#rect = canvas.create_oval(a, fill="red")
speed = 5 # speed of the rectangle
jump = False
crouch=False
    
def keypress(event):
    x = 0
    y = 0
    if event.char == "q": x-= speed
    elif event.char == "d": x+= speed
    elif event.char == "z": y-= speed
    elif event.char == "s":
        crouch=True
    elif event.char == " ":
        diff = 0  ## Difference to initial level
        y = -3    ## Initial speed in y direction
        grav = .1 ## Gravitation
        while diff >= 0:  ## While it is still jumping (higher than initially)
            canvas.move(rect, x, y)
            canvas.update()
            sleep(.01)    ## Pause for 1/100 second
            diff-=y       ## Update current jumping height
            y+=grav       ## Update the speed in y direction
        y = 0 ## Just so it is not moved again, afterwards
    canvas.move(rect, x, y)
    canvas.update()
    canvas.after(1)

window.bind("<Key>", keypress)
window.mainloop()
