#Welcome to Code Cracker!

##How to run
- It is best to run this directly from command line. To do you'll want to start in hw_project -> src -> hw_13
'''
cd src/hw_13
'''
- From there run
'''
python GUI.py
'''
- Note might be python3 instead of python depending on your computer
- From there you should see a screen w/ a inbox for a password as well as options for SHA types and dictionary types.
- Select whatever values you want to. Note the further down the list your phrases are the longer it will take to crack so take a look at the list's in the directory to make your selection.
- A suggestion to start off with is to do the password "aaa" or "aaaalex" against the smallest list as both of these will finish very quickly.
- Once you hit **Start Decoding** a second screen will come up.
- While it says **Loading...** it is working in the background. You can see the words it's testing in the command line.
- Once it's finished it should display a full screen matplot graph with all necessary info.
- Even cooler though, once you've analyzed that data navigate back to the initial window and try another password!
- If you keep the initial window open after the second password is cracked it will display both passwords that you tested.
- This will continue for however many passwords you test. Once you close the initial page your data is gone for good. 
- Additional note. If the matplot graph comes up and it appears to have no bar for the password you just tested, that is most likely due to the scale not showing it's true height.

