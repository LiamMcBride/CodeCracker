from tkinter import *
from Style import Style
from Cracker import Cracker

'''
Result screen GUI for the code cracker project.
Authors: Liam McBride, Patrick Edmonds
Version: 12/01/2021
'''
class BreakingGUI:
    def __init__(self, master, user_password):
        #Sets up backend and begins cracking
        self.cracker = Cracker(user_password, self) 

        #Sets up window
        self.master = master
        master.title("Code Cracker")
        master.minsize(Style.minWidth, Style.minHeight)
        master.configure(background = Style.bgColor)
        self.passedTime = 0

        #Labels
        self.label = Label(
            master,
            text="Currently Cracking",
            height = 2,
            font = (Style.fontType, 25),
            bg = Style.bgColor,
            fg = Style.textColor
            )
        self.label.pack()

        self.lblProgress = Label(
            master,
            text= "Loading...",
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
        self.lblProgress.config(text="Loading...") 
        if(self.passedTime > 30):
            self.cracker.getCrackin()
            self.passedTime = -1       
        if(self.cracker.solved):
            self.lblProgress.config(text= str(self.cracker.getTotalDone()) + " of " + str(self.cracker.getTotalPasswords()) + " Tested")
            self.lblEndPassword.config(text= "The password is " + str(self.cracker.getCurrentPassword()))
            self.lblEndTime.config(text="It was found in " + str(self.cracker.getTime()) + " seconds")
        elif self.cracker.failed:
            self.lblProgress.config(text= "Failed to find password. Try another dictionary.")
        else:
            self.master.after(100, self.clock)
    
