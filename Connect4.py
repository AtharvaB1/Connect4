from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Connect Four")
root.configure(bg="lightblue")
count = 0
buttons = []
clicked = True 
canvases = []
win = False
chips = [[" " for i in range (6)] for j in range(7)]

def disableAll():
    global buttons
    for i in buttons:
        i.config(state=DISABLED)
             
def winCheck(xLocal,yLocal,type):
    global count, win
    countVert = 1
    countHorz = 1
    countsidRite = 1
    countsidLeft = 1
    for k in range(1, 4):
        i = xLocal + k
        if i > 6:
            break
        if chips[i][yLocal] != str(type):
            break
        countHorz += 1
    for k in range(1, 4):
        i = xLocal - k
        if i < 0:
            break
        if chips[i][yLocal] != str(type):
            break
        countHorz += 1
    for k in range(1, 4):
        j = yLocal + k
        if j > 5:
            break
        if chips[xLocal][j] != str(type):
            break
        countVert += 1
    for k in range(1, 4):
        j = yLocal - k
        if j < 0:
            break
        if chips[xLocal][j] != str(type):
            break
        countVert += 1
    for k in range(1, 4):
        i, j = xLocal - k, yLocal + k
        if i < 0 or j > 5:
            break
        if chips[i][j] != str(type):
            break
        countsidLeft += 1
    for k in range(1, 4):
        i, j = xLocal + k, yLocal - k
        if i > 6 or j < 0:
            break
        if chips[i][j] != str(type):
            break
        countsidLeft += 1
        
    for k in range(1, 4):
        i, j = xLocal + k, yLocal + k
        if i > 6 or j > 5:
            break
        if chips[i][j] != str(type):
            break
        countsidRite += 1
    for k in range(1, 4):
        i, j = xLocal - k, yLocal - k
        if i < 0 or j < 0:
            break
        if chips[i][j] != str(type):
            break
        countsidRite += 1
        
    if(countsidLeft>=4 or countsidRite>=4 or countHorz>=4 or countVert>=4):
        win = True
        disableAll()
        if str(type)=="R":
            winstate = messagebox.showinfo("Connect4", "Red has won!")
            if(winstate):
                response = messagebox.askokcancel("Connect4", "Will you try again?")
                if(response):
                    reset()
        else:
            winstate = messagebox.showinfo("Connect4", "Yellow has won!")
            if(winstate):
                response = messagebox.askokcancel("Connect4", "Will you try again?")
                if(response):
                    reset()
        
        
    if count==42 and win == False:
        disableAll()
        winstate = messagebox.showinfo("Connect4","Whomp Whomp, no one won")
        if(winstate):
            response = messagebox.askokcancel("Connect4", "Will you try again?")
            if(response):
                reset()
        
    

def b_click(b):
    global clicked, buttons, count
    for i in range (5,-1,-1):
        if chips[b][i] == " " and clicked == True:
            chips[b][i] =  "R"
            clicked = False
            repaint()
            count+=1
            winCheck(b,i,"R")
            return
        elif chips[b][i] == " " and clicked == False:
            chips[b][i] =  "Y"
            clicked = True
            repaint()
            count+=1
            winCheck(b,i,"Y")
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
   
def reset():
    global clicked, count, canvases, chips, win, buttons
    clicked = True 
    canvases = []
    buttons = []
    win = False
    chips = [[" " for i in range (6)] for j in range(7)]
    count = 0
    for i in range(7):
        canvases.append(Canvas(root,height=670,width=100,bg="lightblue",highlightthickness=0))
        z = canvases[i]
        x = Button(root,text="Drop Checker", font=("Times New Roman",12),height=5,width=10,border=3,highlightthickness=4,bg="SystemButtonFace",command=lambda idx=i: b_click(idx))
        buttons.append(x)
        buttons[i].grid(column=i,row=0)
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
    buttons.append(x)
    buttons[i].grid(column=i,row=0)
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