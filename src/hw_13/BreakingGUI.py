from tkinter import *
from Style import Style
from Cracker import Cracker

class BreakingGUI:
    def __init__(self, master, user_password):
        self.master = master
        master.title("Code Cracker")
        master.minsize(Style.minWidth, Style.minHeight)
        master.configure(background = Style.bgColor)
        self.passedTime = 0

        

        self.label = Label(
            master,
            text="Currently Cracking",
            height = 2,
            font = (Style.fontType, 25),
            bg = Style.bgColor,
            fg = Style.textColor
            )
        self.label.pack()

        self.cracker = Cracker(user_password)

        self.lblProgress = Label(
            master,
            text= str(self.cracker.getTotalDone()) + " of " + str(self.cracker.getTotalPasswords()) + " Tested\n" + str(self.cracker.getTime()),
            height = 2,
            font = (Style.fontType, 15),
            bg = Style.bgColor,
            fg = Style.textColor
            )
        self.lblProgress.pack()

        self.lblEndPassword = Label(
        self.master,
        text="",
        height = 2,
        font = (Style.fontType, 15),
        bg = Style.bgColor,
        fg = Style.textColor
        )
        self.lblEndPassword.pack()

        self.lblEndTime = Label(
        self.master,
        text="",
        height = 2,
        font = (Style.fontType, 15),
        bg = Style.bgColor,
        fg = Style.textColor
        )
        self.lblEndTime.pack()

        

        

    def clock(self):
        if(self.passedTime > -1):
            self.passedTime += 1
        self.lblProgress.config(text= str(self.cracker.getTotalDone()) + " of " + str(self.cracker.getTotalPasswords()) + " Tested\n" + str(self.cracker.getTime()))
        #self.lblCurrentPassword.config(text= self.cracker.getCurrentPassword())
        if(self.cracker.getTime() != 0):
            self.lblEndPassword.config(text= "The password is " + str(self.cracker.getCurrentPassword()))
            self.lblEndTime.config(text="It was found in " + str(self.cracker.getTime()) + " seconds")
        if(self.passedTime > 30):
            self.cracker.getCrackin()
            self.passedTime = -1
        self.master.after(100, self.clock)