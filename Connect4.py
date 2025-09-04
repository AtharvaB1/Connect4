from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Connect Four")

count = 0
clicked = True 
buttons = []
canvases = []
chips = [[" " for i in range (7)] for j in range(6)]

def reset():
    global clicked, count, buttons, butCount
    buttons = []
    clicked = True
    count = 0
    butCount = 0
    for i in range(7):
        buttons.append(Button(root,text="Drop Checker", font=("Times New Roman",12),height=5,width=10,border=3,highlightthickness=4,bg="SystemButtonFace",command=lambda: b_click(buttons[i])))  
        canvases.append(Canvas(root,height=1000,width=120))
        x = buttons[i]
        x.grid(column=i,row=0)
    
def checkWin(dir,count):
    pass

def b_click(b):
    pass

for i in range(7):
    #buttons.append(Button(root,text=" ", font=("Times New Roman",12),height=4,width=8,bg="SystemButtonFace",command=lambda: b_click(buttons[i])))
    buttons.append(Button(root,text="Drop Checker", font=("Times New Roman",12),height=5,width=10,border=3,highlightthickness=4,bg="SystemButtonFace",command=lambda: b_click(buttons[i])))  
    canvases.append(Canvas(root,height=670,width=100))
    z = canvases[i]
    x = buttons[i]
    x.grid(column=i,row=0)
    z.grid(column=i,row=1)

    z.create_oval(2,10,100,110)
    z.create_oval(2,120,100,220)
    z.create_oval(2,230,100,330)
    z.create_oval(2,340,100,440)
    z.create_oval(2,450,100,550)
    z.create_oval(2,560,100,660)
    

my_menu = Menu(root)
root.config(menu=my_menu)
option_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options",menu=option_menu)
option_menu.add_command(label="Reset", command=reset)

root.mainloop()