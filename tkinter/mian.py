import tkinter as tk
from tkinter import *
from tkinter import ttk

MOUSE_BTN = '<Button-'
MOUSE_LEFT_BTN = MOUSE_BTN+'1>'
MOUSE_RIGHT_BTN = MOUSE_BTN+'3>'
MOUSE_SCROLL_BTN = MOUSE_BTN+'2>'


class Block:
    'Class description'
    def __init__(self):
        'Class Block constructor'
        self.win = tk.Tk()
        self.win.geometry('800x600')

        self.optionsmenu_add(self.win)
        self.label_add(self.win)
        self.button_add(self.win)
        self.entry_add(self.win)
        self.tex_box_add(self.win)
        self.combobox_add(self.win)
        self.win.mainloop()
        

    def optionsmenu_add(self, win):
        self.optionlist = ['one','two','three']
        veriable = tk.StringVar(win)
        veriable.set('123')
        self.combo = tk.OptionMenu(
            win,
            veriable,
            *self.optionlist)
        self.combo.pack()
        self.combo.place(x = 300, y = 0, width = 100)
##        self.combo.
##
    def combobox_add(self, win):
        print('add combo')
        
        self.cmbb = ttk.Combobox(self.win, values = ['0','1','2'])
        self.cmbb.pack(padx=0, pady=50)
        self.cmbb.bind('<<ComboboxSelected>>', self.ComboSelectedEvt)
        self.cmbb.current(1)
        print(self.cmbb.current())
        print(self.cmbb.get())

    def ComboSelectedEvt(self,event):
        print('ComboSelectedEvt:', event)
        print(self.cmbb.get())

    def ComboAddItem(self, item):
        vals = list(self.cmbb['values'])
        vals.append(item)
        self.cmbb['values'] = vals
        print(self.cmbb['values'])

    def label_add(self, win):
        self.lbl = tk.Label(
            win,
            text = 'LABEL',
            foreground = 'white',
            background = 'black',
            width = 10,
            height = 1)
        self.lbl.pack()#(side = 'left')
        self.lbl.place(x = 0, y = 0, width = 50, height = 25,)

    def button_add(self, win):
        self.btn = tk.Button(
            win,
            text = 'BUTTON',
            bg = 'blue',
            fg = 'yellow')
        self.btn.bind(MOUSE_LEFT_BTN, self.btn_press_evt)
        self.btn.pack()
        self.btn.place(x = 100, y = 0, width = 50, height = 25,)

    def entry_add(self, win):
        self.entry = tk.Entry()
        self.entry.pack()
        self.entry.place(x = 200, y = 0, width = 50, height = 25)
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
        self.text_box.place(x = 0, y = 100, width = 500, height = 250)
        scroll = tk.Scrollbar(command = self.text_box.yview)
        scroll.pack(side = RIGHT, fill = Y)
        self.text_box.config(yscrollcommand = scroll.set)

    def btn_press_evt(self, event):
        entry_text = self.entry.get()
        text = self.text_box.get(1.0, END)
        self.text_box.delete(1.0, END)
        text = text + entry_text
        self.text_box.insert(1.0,text)
        self.ComboAddItem(text)
        print(text)
        print(event)
##        self.win.withdraw() # скрыть окно


def main():
##    x = 's'
##    print(dir(x))
    print(Block.__doc__)
    print(Block.__init__.__doc__)
    
##    window = tk.Tk()
##    window.title('title')

    block = Block()
##    print(dir(block))
    
##    window.mainloop()
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
