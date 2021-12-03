from tkinter import *
from Style import Style
from Cracker import Cracker
import matplotlib.pyplot as plt

'''
Result screen GUI for the code cracker project.
Authors: Liam McBride, Patrick Edmonds
Version: 12/01/2021
'''
class BreakingGUI:
    def __init__(self, master, user_password, sha, dictionary, times, passwords):
        #Sets up backend and begins cracking
        self.cracker = Cracker(user_password, sha, dictionary)

        #Sets up window
        self.master = master
        master.title("Code Cracker")
        master.minsize(Style.minWidth, Style.minHeight)
        master.configure(background = Style.bgColor)

        #Sets up fields
        self.sha = sha
        self.times = times
        self.passwords = passwords
        self.dictionary = dictionary
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

        
    #This function runs like a clock. Running every 100 miliseconds to check for updates in the backend
    def clock(self):
        if(self.passedTime > -1):
            self.passedTime += 1
        self.lblProgress.config(text="Loading...") 
        #Starts the backend after a slight delay to let the window load
        if(self.passedTime > 30):
            self.cracker.getCrackin()
            self.passedTime = -1
        #When it is solved the matplot is displayed       
        if(self.cracker.solved):
            self.times.append(self.cracker.getTime())
            self.passwords.append(self.cracker.getCurrentPassword() + " w/ " + self.sha +
             "\nUsing: " + self.dictionary + " Using " + str(self.cracker.getTotalDone())
              + " guesses")
            plt.bar(self.passwords, self.times)
            plt.ylabel('Time (Seconds)')
            plt.xlabel('Password')
            mng = plt.get_current_fig_manager()
            plt.show()
        #Displays failure to user
        elif self.cracker.failed:
            self.lblProgress.config(text= "Failed to find password. Try another dictionary.")
        #Keeps the clock ticking
        else:
            self.master.after(100, self.clock)
    
