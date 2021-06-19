import tkinter as tk
from tkinter import *

MOUSE_BTN = '<Button-'
MOUSE_LEFT_BTN = MOUSE_BTN+'1>'
MOUSE_RIGHT_BTN = MOUSE_BTN+'3>'
MOUSE_SCROLL_BTN = MOUSE_BTN+'2>'


class Block:
    'Class description'
    def __init__(self, window):
        'Class Block constructor'
        self.win = window
        self.label_add(window)
        self.button_add(window)
        self.entry_add(window)
        self.tex_box_add(window)

    def label_add(self, win):
        self.lbl = tk.Label(
            win,
            text = 'LABEL',
            foreground = 'white',
            background = 'black',
            width = 50,
            height = 10)
        self.lbl.pack()

    def button_add(self, win):
        self.btn = tk.Button(
            win,
            text = 'BUTTON',
            width = 25,
            height = 5,
            bg = 'blue',
            fg = 'yellow')
        self.btn.bind(MOUSE_LEFT_BTN, self.btn_press_evt)
        self.btn.pack()

    def entry_add(self, win):
        self.entry = tk.Entry()
        self.entry.pack()
##        self.entry.insert(0,'text')
##        self.name = entry.get()

    def tex_box_add(self, win):
        self.text_box = tk.Text(
            win,
            height = 10)
##        self.text_box.pack(side = LEFT)
##
##        self.scroll = tk.Scrollbar(command = self.text_box.yview)
##        self.scroll.pack(side = LEFT, fill = Y)
        self.text_box.pack(side = LEFT)

        scroll = tk.Scrollbar(command = self.text_box.yview)
        scroll.pack(side = LEFT, fill = Y)

        self.text_box.config(yscrollcommand = scroll.set)

    def btn_press_evt(self, event):
        entry_text = self.entry.get()
        text = self.text_box.get(1.0, END)
        self.text_box.delete(1.0, END)
        text = text + entry_text
        self.text_box.insert(1.0,text)
        print(text)
        print(event)
##        self.win.withdraw() # скрыть окно


def main():
##    x = 's'
##    print(dir(x))
    print(Block.__doc__)
    print(Block.__init__.__doc__)
    
    window = tk.Tk()
    window.title('title')

    block = Block(window)
    print(dir(block))
    
    window.mainloop()
## ---------------------------------------------------------------------
##    frame = tk.Frame()
##    
##    frame_label = tk.Label(
##        master = frame,
##        text = 'frame_label')
##    frame_label.pack()
##    
##    frame.pack()
## ---------------------------------------------------------------------
    




if __name__ == "__main__":
    main()
