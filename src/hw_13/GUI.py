from tkinter import *
from BreakingGUI import BreakingGUI
from Style import Style

'''
Set up GUI for the code cracker project.
Authors: Liam McBride, Patrick Edmonds
Version: 12/01/2021
'''
class GUI:
    def __init__(self, master):
        #Window set up
        self.master = master
        master.title("Code Cracker")        
        master.minsize(Style.minWidth, Style.minHeight)
        master.configure(background = Style.bgColor)  

        #Fields
        self.times = []
        self.passwords = []      

        #Label and button set up
        self.label = Label(
            master,
            text="Welcome to Code Cracker",
            height = 2,
            font = (Style.fontType, 25),
            bg = Style.bgColor,
            fg = Style.textColor
            ).pack()

        self.label2 = Label(
            master,
            text="Please enter desired password:",
            height = 2,
            font = (Style.fontType, 15),
            bg = Style.bgColor,
            fg = Style.textColor
            ).pack()

        self.pword = StringVar(master, "")

        self.password_input = Entry(
            master,
            font = (Style.fontType, 15),
            text="password",
            textvariable= self.pword
        ).pack()

        self.spacer = Label(
            master,            
            height = 2,
            bg = Style.bgColor,
            ).pack()

        self.label2 = Label(
            master,
            text="Choose SHA Encoding:",
            height = 2,
            font = (Style.fontType, 15),
            bg = Style.bgColor,
            fg = Style.textColor
            ).pack()

        self.set1 = StringVar(master, "SHA256")

        self.rad1 = Radiobutton(
                master,
                text="SHA 256",
                variable = self.set1,
                value = "sha256",
                indicator = 0,
                command = None,
                bg = Style.bgColor,
                fg = Style.textColor,
                font = (Style.fontType, 10)
            ).pack()

        self.rad2 = Radiobutton(
                master,
                text="SHA 512",
                variable = self.set1,
                value = "sha512",
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

        self.set2 = StringVar(master, "small_list.txt")

        self.rad3 = Radiobutton(
                master,
                text="1000 Passwords",
                variable = self.set2,
                value = "small_list.txt",
                indicator = 0,
                command = None,
                width=15,
                bg = Style.bgColor,
                fg = Style.textColor,
                font = (Style.fontType, 10)
            ).pack()

        self.rad4 = Radiobutton(
                master,
                text="10,000 Passwords",
                variable = self.set2,
                value = "10k_list.txt",
                indicator = 0,
                command = None,
                width=15,
                bg = Style.bgColor,
                fg = Style.textColor,
                font = (Style.fontType, 10)
            ).pack()

        self.rad5 = Radiobutton(
                master,
                text="100,000 Passwords",
                variable = self.set2,
                value = "100k_list.txt",
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

    #Sends settings and file name to the BreakingGUI
    def startDecode(self):
        root2 = Tk()
        print(str(self.set1.get()) + " " + str(self.set2.get()) + " " + self.pword.get())
        window2 = BreakingGUI(root2, self.pword.get(), self.set1.get(), self.set2.get(), self.times, self.passwords)
        window2.clock()
        root2.mainloop()
        

#Starts the program
root = Tk()
gui = GUI(root)
root.mainloop() 