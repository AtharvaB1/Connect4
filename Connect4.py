from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Connect Four")
root.configure(bg="lightblue")
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
            #winCheck("None", 0, i, b)
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
                z.create_oval(0,a,99,b)
            elif(chips[i][j] == "R"):
                a = 100*j + 10 + 10*j
                b = 110 + 100*j + 10*j
                z.create_oval(0,a,99,b, fill="red")
            elif(chips[i][j] == "Y"):
                a = 100*j + 10 + 10*j
                b = 110 + 100*j + 10*j
                z.create_oval(0,a,99,b, fill="yellow")
                
def winCheck(xLocal, yLocal,type):
    countVert = 0
    countHorz = 0
    countsidRite = 0
    countsidLeft = 0
    xMax = xLocal+3
    xMin = xLocal-3
    yMax = yLocal+3
    yMin = yLocal-3
    if xMax>=7:
        xMax=7
    if yMax>=7:
        yMax=7
    if yMin<=-1:
        yMin=-1
    if xMin<=-1:
        xMin=-1
    for i in range(i,xMax,1):
        pass #checks right
    for i in range(i,xMin,-1):
        pass #check left
    for i in range(i,yMax,1):
        pass #check up
    for i in range(i,yMin,-1):
        pass #check down
    for i in range(i,xMax,1):
        for i in range(i,yMax,1):
            pass #check up right, sidRight
        for i in range(i,yMin,-1):
            pass #check down right, sidLeft
    for i in range(i,xMin,-1):
        for i in range(i,yMax,1):
            pass #check up left, sidleft
        for i in range(i,yMin,-1):
            pass #check down right, sidright
    
        
    
def reset():
    global clicked, count, canvases, chips, win
    clicked = True 
    canvases = []
    win = False
    chips = [[" " for i in range (6)] for j in range(7)]
    count = 0
    for i in range(7):
        canvases.append(Canvas(root,height=670,width=100,bg="lightblue",highlightthickness=0))
        z = canvases[i]
        x = Button(root,text="Drop Checker", font=("Times New Roman",12),height=5,width=10,border=3,highlightthickness=4,bg="SystemButtonFace",command=lambda idx=i: b_click(idx))
        x.grid(column=i,row=0)
        z.grid(column=i,row=1)
        z.create_oval(0,10,99,110,fill="white")
        z.create_oval(0,120,99,220,fill="white")
        z.create_oval(0,230,99,330,fill="white")
        z.create_oval(0,340,99,440,fill="white")
        z.create_oval(0,450,99,550,fill="white")
        z.create_oval(0,560,99,660,fill="white")

for i in range(7):
    canvases.append(Canvas(root,height=670,width=100,bg="lightblue",highlightthickness=0))
    z = canvases[i]
    x = Button(root,text="Drop Checker", font=("Times New Roman",12),height=5,width=10,border=3,highlightthickness=4,bg="SystemButtonFace",command=lambda idx=i: b_click(idx))
    x.grid(column=i,row=0)
    z.grid(column=i,row=1)
    z.create_oval(0,10,99,110,fill="white")
    z.create_oval(0,120,99,220,fill="white")
    z.create_oval(0,230,99,330,fill="white")
    z.create_oval(0,340,99,440,fill="white")
    z.create_oval(0,450,99,550,fill="white")
    z.create_oval(0,560,99,660,fill="white")
    

my_menu = Menu(root)
root.config(menu=my_menu)
option_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options",menu=option_menu)
option_menu.add_command(label="Reset", command=reset)

root.mainloop()