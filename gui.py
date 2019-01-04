from tkinter import *

root = Tk()

root.title('APP')

root.geometry('500x400')

title = Label(text='label text')
title.grid()

def Hello(event):
    print ("Yet another hello world")

btn = Button(root,
             text='Click me',
             width=5,height=5,
             bg='white',fg='black')

btn.bind('<Button-1>', Hello)
#btn.pack()
root.mainloop()
