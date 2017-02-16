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

        self.editor = Label(background=BACKGROUND, font=FONT, padx=1000, pady=1000)
        self.editor.grid()

        self.root.mainloop()
