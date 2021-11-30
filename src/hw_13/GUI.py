from tkinter import *

class GUI:
    def __init__(self, master):
        self.fontType = "Ariel"
        self.minWidth = 1000
        self.minHeight = 600
        self.bgColor = "#17223B"
        self.fgColor = "#263859"
        self.textColor = "#FF6768"
        self.master = master
        master.title("Code Cracker")
        #master.geometry(self.screenSize)
        master.minsize(self.minWidth, self.minHeight)
        master.configure(background = self.bgColor)
        #master.attributes('-fullscreen', True)

        self.label = Label(
            master,
            text="Welcome to Code Cracker",
            height = 2,
            font = (self.fontType, 25),
            bg = self.bgColor,
            fg = self.textColor
            )
        #.grid(column=4)
        self.label.pack()

        self.label2 = Label(
            master,
            text="Please enter desired password:",
            height = 2,
            font = (self.fontType, 15),
            bg = self.bgColor,
            fg = self.textColor
            )
        self.label2.pack()

        self.input = Entry(
            master,
            font = (self.fontType, 15),
            text="password",
        )
        self.input.pack()

        self.spacer = Label(
            master,            
            height = 2,
            bg = self.bgColor,
            )
        self.spacer.pack()

        self.label2 = Label(
            master,
            text="Choose SHA Encoding:",
            height = 2,
            font = (self.fontType, 15),
            bg = self.bgColor,
            fg = self.textColor
            )
        self.label2.pack()

        v = StringVar(master, "1")

        choices = {"SHA 5" : "1",
                    "SHA 2" : "2"}

        for (text, value) in choices.items():
            Radiobutton(
                master,
                text=text,
                variable = v,
                value = value,
                indicator = 0,
                command = None,
                bg = self.bgColor,
                fg = self.textColor,
                font = (self.fontType, 10)
            ).pack()

        self.spacer = Label(
            master,            
            height = 10,
            bg = self.bgColor,
            )
        self.spacer.pack()

        self.close_button = Button(
            master,
            text="Quit",
            command=master.quit,
            font = (self.fontType, 10),
            bg = self.bgColor,
            fg = self.textColor
            )
        self.close_button.pack()



    def shaValue(self, value):
        print(value)

    def greet(self):
        print("Greetings!")

root = Tk()
gui = GUI(root)
root.mainloop()