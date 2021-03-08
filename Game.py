from tkinter import *
from tkinter import ttk
from tkinter import messagebox
aplayer1=1 #set active player
p1=[] #player 1
p2=[] #player 2





#design Game dy code hussain alsamr
root=Tk()
root.title("Tic Tac Player 1")
style=ttk.Style()
style.theme_use('alt')








bu1=ttk.Button(root,text='')
bu1.grid(row=0,column=0,sticky='snew',ipady=40,)#button 1
bu1.config(command=lambda: bu(1))


bu2=ttk.Button(root,text='')
bu2.grid(row=0,column=1,sticky='snew',ipady=40,)#button 2
bu2.config(command=lambda: bu(2))

bu3=ttk.Button(root,text='')
bu3.grid(row=0,column=2,sticky='snew',ipady=40,)#button 3
bu3.config(command=lambda: bu(3))

bu4=ttk.Button(root,text='')
bu4.grid(row=1,column=0,sticky='snew',ipady=40,)#button 4
bu4.config(command=lambda: bu(4))

bu5=ttk.Button(root,text='')
bu5.grid(row=1,column=1,sticky='snew',ipady=40,)#button 5
bu5.config(command=lambda: bu(5))

bu6=ttk.Button(root,text='')
bu6.grid(row=1,column=2,sticky='snew',ipady=40,)#button 6
bu6.config(command=lambda: bu(6))


bu7=ttk.Button(root,text='')
bu7.grid(row=2,column=0,sticky='snew',ipady=40,)#button 7
bu7.config(command=lambda: bu(7))


bu8=ttk.Button(root,text='')
bu8.grid(row=2,column=1,sticky='snew',ipady=40,)#button 8
bu8.config(command=lambda: bu(8))


bu9=ttk.Button(root,text='')
bu9.grid(row=2,column=2,sticky='snew',ipady=40,)#button 9
bu9.config(command=lambda: bu(9))


def bu(id):

    global aplayer1
    global p1
    global p2
    if aplayer1==1:
        set_x(id,'X')
        p1.append(id)
        root.title('Tic Tac Player 2')
        aplayer1=2
        print ('p1:',format(p1))

    elif aplayer1 == 2:
        set_x(id,'O')
        p2.append(id)
        root.title('Tic Tac Player 1')
        aplayer1 = 1
        print('p2:', format(p2))

def set_x(id,text):
    if id==1:
        bu1.config(text=text)
        bu1.state(['disabled'])
    elif id == 2:
       bu2.config(text=text)
       bu2.state(['disabled'])
    elif id == 3:
       bu3.config(text=text)
       bu3.state(['disabled'])
    elif id == 4:
       bu4.config(text=text)
       bu4.state(['disabled'])
    elif id == 5:
        bu5.config(text=text)
        bu5.state(['disabled'])
    elif id == 6:
        bu6.config(text=text)
        bu6.state(['disabled'])
    elif id ==7:
        bu7.config(text=text)
        bu7.state(['disabled'])
    elif id == 8:
       bu8.config(text=text)
       bu8.state(['disabled'])

    elif id ==9:
       bu9.config(text=text)
       bu9.state(['disabled'])

def winer():
    winer=-1

    if ((1 in p1) and (2 in p1) and (3 in p1)):
        winer=1
    if (1 in p2 and 2 in p2 and 3 in p2):
        winer=2
    if (4 in p1 and 5 in p1 and 6 in p1):
        winer=1
    if (4 in p2 and 5 in p2 and 6 in p2):
        winer=2
    if (7 in p1 and 8 in p1 and 9 in p1):
        winer=1
    if (7 in p2 and 8 in p2 and 9 in p2):
        winer=2
    if (1 in p1 and 4 in p1 and 7 in p1):
        winer=1
    if (1 in p2 and 4 in p2 and 7 in p2):
        winer=2
    if (2 in p1 and 5 in p1 and 8 in p1):
        winer=1
    if (2 in p2 and 5 in p2 and 8 in p2):
        winer=2
    if (3 in p1 and 6 in p1 and 9 in p1):
        winer=1
    if (3 in p2 and 6 in p2 and 9 in p2):
        winer=2
    if (1 in p1 and 5 in p1 and 9 in p1):
        winer = 1
    if (1 in p2 and 5 in p2 and 9 in p2):
        winer = 2

    if winer==1:
      messagebox.showinfo(title="Cong.",message='player 1 is Winer ')



root.mainloop()