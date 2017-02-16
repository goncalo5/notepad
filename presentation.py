from Tkinter import *
from constants import *


class Menu(object):
    def __init__(self):
        self.root = Tk()
        self.root.title('NotePad')

        w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        #self.root.overrideredirect(1)
        #self.root.geometry("%dx%d+0+0" % (w, h))
        #self.root.focus_set()
        self.root.configure(background=BACKGROUND)

        self.root.mainloop()
