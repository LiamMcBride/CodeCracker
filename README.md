# Welcome to Code Cracker!
Made by Liam McBride and Patrick Edmonds
## How to run
- It is best to run this directly from command line because of how the file system works.
- It has worked in both eclipse and VS code as well though. But if there are issues just use command line
- To do this you'll want to start in hw_project -> src -> hw_13
```
cd src/hw_13
```
- From there run
```
python GUI.py
```
- Note might be python3 instead of python depending on your computer
- From there you should see a screen w/ a inbox for a password as well as options for SHA types and dictionary types.
- Select whatever values you want to. Note the further down the dictionary list your phrases are the longer it will take to crack so take a look at the list's in the directory to make your selection. This goes for combos as well. Combos will take longer to crack.
- A suggestion to start off with is to do the password "aaa" or "aaaalex" against the smallest list as both of these will finish very quickly.
- A good medium 20-30 result is to do "passwordmustang" from the 10k list.
- Once you hit **Start Decoding** a second screen will come up.
- While it says **Loading...** it is working in the background. You can see the words it's testing in the command line.
- Once it's finished it should display a full screen matplot graph with all necessary info.
- Even cooler though, once you've analyzed that data navigate back to the initial window and try another password!
- If you keep the initial window open after the second password is cracked it will display both passwords that you tested.
- This will continue for however many passwords you test allowing easy comparison between passwords, dictionaries, and SHA types. Once you close the initial page your data is gone for good. 
- Additional note. If the matplot graph comes up and it appears to have no bar for the password you just tested, that is most likely due to the scale not showing it's true height. Especially if another password took something like 10+ seconds to crack.

## The files
- [GUI.py](src/hw_13/GUI.py): Collects user input, as well as stores the array of previous passwords and stats.
- [BreakingGUI.py](src/hw_13/BreakingGUI.py): Show's the user that the program is running as well as connects the user input and front end to the backend. Additionally handles the display of the results from the backend.
- [Cracker.py](src/hw_13/Cracker.py): This is the backend and the actual logic behind the program
- [small_list, 10k_list, 100k_list](small_list.txt): The dictionaries being read from.
