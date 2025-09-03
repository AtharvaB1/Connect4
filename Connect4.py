from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Connect Four")

count = 0
clicked = True 
buttons = []
butCount = 0

def reset():
    global clicked, count, buttons, butCount
    buttons = []
    clicked = True
    count = 0
    butCount = 0
    for i in range(42):
        buttons.append(Button(root,text=" ", font=("Times New Roman",12),height=4,width=8,bg="SystemButtonFace",command=lambda: b_click(buttons[i]))) 
    for i in range(6):
        for j in range(7):
            z = buttons[butCount]
            z.grid(row=i,column=j)
            butCount+=1
    
def checkWin(dir,count):
    pass

def b_click(b):
    pass

for i in range(42):
    #buttons.append(Button(root,text=" ", font=("Times New Roman",12),height=4,width=8,bg="SystemButtonFace",command=lambda: b_click(buttons[i])))
    buttons.append(Button(root,text=" ", font=("Times New Roman",12),height=4,width=8,border=3,highlightthickness=4,bg="SystemButtonFace",command=lambda: b_click(buttons[i])))  
for i in range(6):
    for j in range(7):
        z = buttons[butCount]
        z.grid(row=i,column=j,padx=10,pady=10)
        butCount+=1

my_menu = Menu(root)
root.config(menu=my_menu)
option_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options",menu=option_menu)
option_menu.add_command(label="Reset", command=reset)

root.mainloop()