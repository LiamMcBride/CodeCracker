from tkinter import Tk, Label, Button

class GUI:
    def __init__(self, master):
        self.fontType = "Ariel"
        self.minWidth = 1000
        self.minHeight = 600
        self.gray = "#202124"
        self.master = master
        master.title("Code Cracker")
        #master.geometry(self.screenSize)
        master.minsize(self.minWidth, self.minHeight)
        master.configure(background = self.gray)
        #master.attributes('-fullscreen', True)

        self.label = Label(
            master,
            text="Welcome to Code Cracker",
            height = 2,
            font = (self.fontType, 25),
            bg = self.gray,
            fg = "white"
            )
        self.label.pack()


        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="close", command = master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")

root = Tk()
gui = GUI(root)
root.mainloop()