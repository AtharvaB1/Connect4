from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Connect Four")
count = 0
clicked = True 
canvases = []
win = False
chips = [[" " for i in range (6)] for j in range(7)]

def b_click(b):
    global clicked
    for i in range (5,-1,-1):
        if chips[b][i] == " " and clicked == True:
            chips[b][i] =  "R"
            clicked = False
            repaint()
            winCheck("None", 0, i, b)
            return
        elif chips[b][i] == " " and clicked == False:
            chips[b][i] =  "Y"
            clicked = True
            repaint()
            return

def repaint():
    global canvases
    for i in range(len(chips)):
        z = canvases[i]
        for j in range(len(chips[0])):
            if(chips[i][j] == " "):
                a = 100*j + 10 + 10*j
                b = 110 + 100*j + 10*j
                z.create_oval(2,a,100,b)
            elif(chips[i][j] == "R"):
                a = 100*j + 10 + 10*j
                b = 110 + 100*j + 10*j
                z.create_oval(2,a,100,b, fill="red")
            elif(chips[i][j] == "Y"):
                a = 100*j + 10 + 10*j
                b = 110 + 100*j + 10*j
                z.create_oval(2,a,100,b, fill="yellow")
                
def winCheck(dir, count, xLocal, yLocal):
    pass     
    
def reset():
    global clicked, count, canvases, chips, win
    clicked = True 
    canvases = []
    win = False
    chips = [[" " for i in range (6)] for j in range(7)]
    count = 0
    for i in range(7):
        canvases.append(Canvas(root,height=670,width=100))
        z = canvases[i]
        x = Button(root,text="Drop Checker", font=("Times New Roman",12),height=5,width=10,border=3,highlightthickness=4,bg="SystemButtonFace",command=lambda idx=i: b_click(idx))
        x.grid(column=i,row=0)
        z.grid(column=i,row=1)
        z.create_oval(2,10,100,110)
        z.create_oval(2,120,100,220)
        z.create_oval(2,230,100,330)
        z.create_oval(2,340,100,440)
        z.create_oval(2,450,100,550)
        z.create_oval(2,560,100,660)

for i in range(7):
    canvases.append(Canvas(root,height=670,width=100))
    z = canvases[i]
    x = Button(root,text="Drop Checker", font=("Times New Roman",12),height=5,width=10,border=3,highlightthickness=4,bg="SystemButtonFace",command=lambda idx=i: b_click(idx))
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