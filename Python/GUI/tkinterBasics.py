from tkinter import *
from PIL import Image, ImageTk

class NewWindow(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window_layout()

    def init_window_layout(self):
        self.master.title("GUI Tutorial")
        self.pack(fill=BOTH, expand=1)
        quitButton = Button(self, text='Quit', command=self.window_exit)
        quitButton.place(x=500, y=400)
        self.menu_layout()

    def menu_layout(self):
        menu = Menu(self.master)
        self.master.config(menu = menu)

        file = Menu(menu)
        file.add_command(label='New')
        file.add_command(label='Open')
        file.add_command(label='Save')
        file.add_command(label='Exit', command = self.window_exit)
        menu.add_cascade(label='File', menu=file)

        edit = Menu(menu)
        edit.add_command(label='Undo')
        edit.add_command(label='Show Image', command = self.showImage)
        edit.add_command(label='Show Text', command = self.showText)
        menu.add_cascade(label='Edit', menu=edit)

    def showImage(self):
        load = Image.open('rupee.jpg')
        render = ImageTk.PhotoImage(load)

        img = Label(self, image=render)
        img.image = render
        img.place(x=30,y=30)

    def showText(self):
        text = Label(self, text="Hello World!!")
        text.pack()
        
    def window_exit(self):
        exit()

# Tk() makes a main or master Frame
root = Tk()
root.geometry("1000x600")

app = NewWindow(root)

# Runs an inifinite loop to process events on main frame
root.mainloop()


