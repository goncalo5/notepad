from Tkinter import *
from constants import *


class Menu(object):
    def __init__(self):
        self.root = Tk()
        self.root.title('NotePad')

        w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        #self.root.overrideredirect(1)
        self.root.geometry(SIZE)
        #self.root.focus_set()
        #self.root.configure(background='gray')

        self.canvas = Canvas(self.root, width=50, height=200)
        self.canvas.focus_force()
        self.canvas.grid(columnspan=4)
        self.canvas.bind('<Key>', self.write)

        self.editor = Label(self.root, text='sad',
                            background=BACKGROUND, fg='white',
                            font=FONT, padx=100, pady=100)
        self.editor.grid()

        self.root.mainloop()


    def write(self, event):
        op = {'plus': '+', 'minus': '-', 'asterisk': '*', 'slash': '/', 'period': '.'}
        char = event.keysym
        print char
        if char == '??':
            return
        elif char == 'Return':
            self.equal()
        elif char == 'BackSpace':
            self.ac()
        else:
            if char in op:
                char = op[char]
            self.print_value(char)

    def print_value(self, character):
        self.editor['text'] += character