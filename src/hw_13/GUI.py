from tkinter import *
from BreakingGUI import BreakingGUI
from Style import Style

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Code Cracker")
        #master.geometry(Style.screenSize)
        master.minsize(Style.minWidth, Style.minHeight)
        master.configure(background = Style.bgColor)
        #master.attributes('-fullscreen', True)

        self.label = Label(
            master,
            text="Welcome to Code Cracker",
            height = 2,
            font = (Style.fontType, 25),
            bg = Style.bgColor,
            fg = Style.textColor
            )
        #.grid(column=4)
        self.label.pack()

        self.label2 = Label(
            master,
            text="Please enter desired password:",
            height = 2,
            font = (Style.fontType, 15),
            bg = Style.bgColor,
            fg = Style.textColor
            )
        self.label2.pack()

        self.input = Entry(
            master,
            font = (Style.fontType, 15),
            text="password",
        )
        self.input.pack()

        self.spacer = Label(
            master,            
            height = 2,
            bg = Style.bgColor,
            )
        self.spacer.pack()

        self.label2 = Label(
            master,
            text="Choose SHA Encoding:",
            height = 2,
            font = (Style.fontType, 15),
            bg = Style.bgColor,
            fg = Style.textColor
            )
        self.label2.pack()

        v = StringVar(master, "1")

        choices = {"SHA 256" : "1",
                    "SHA 512" : "2"}

        for (text, value) in choices.items():
            Radiobutton(
                master,
                text=text,
                variable = v,
                value = value,
                indicator = 0,
                command = None,
                bg = Style.bgColor,
                fg = Style.textColor,
                font = (Style.fontType, 10)
            ).pack()

        self.spacer = Label(
        master,            
        height = 2,
        bg = Style.bgColor,
        )
        self.spacer.pack()

        self.label2 = Label(
            master,
            text="Choose a Dictionary:",
            height = 2,
            font = (Style.fontType, 15),
            bg = Style.bgColor,
            fg = Style.textColor
            )
        self.label2.pack()

        v = StringVar(master, "1")
        choices = {
            "1000 Passwords": "1",
            "10,000 Passwords": "2",
            "100,000 Passwords": "3"
        }

        for (text, value) in choices.items():
            Radiobutton(
                master,
                text=text,
                variable = v,
                value = value,
                indicator = 0,
                command = None,
                width=15,
                bg = Style.bgColor,
                fg = Style.textColor,
                font = (Style.fontType, 10)
            ).pack()

        self.spacer = Label(
            master,            
            height = 2,
            bg = Style.bgColor,
            )
        self.spacer.pack()

        self.startButton = Button(
            master,
            text="Start Decoding",
            command=self.startDecode,
            font = (Style.fontType, 10),
            bg = Style.bgColor,
            fg = Style.textColor
        ).pack()
        

        self.spacer = Label(
            master,            
            height = 1,
            bg = Style.bgColor,
            )
        self.spacer.pack()

        self.close_button = Button(
            master,
            text="Quit",
            command=master.quit,
            font = (Style.fontType, 10),
            bg = Style.bgColor,
            fg = Style.textColor
            )
        self.close_button.pack()

        self.spacer = Label(
            master,            
            height = 1,
            bg = Style.bgColor,
            )
        self.spacer.pack()



    def startDecode(self):
        root2 = Tk()
        window2 = BreakingGUI(root2, "epson")
        window2.clock()
        root2.mainloop()
        
        


root = Tk()
gui = GUI(root)
root.mainloop()