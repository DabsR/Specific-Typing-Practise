#Code partially tested. Two or three logic errors remain.

from time import time
import levels

selectedIndex = 0
selectedLevel = levels
width = 0
depth = 0
def checkinp(disp, errlambda) :
    inp = ""
    while True :
        inp = input(disp)
        if errlambda(inp):
            print("Proceeding...")
            return inp
        else:
            print("<!> Incorrect Input <!>")

def defaultValues():
    selectedIndex = 5
    selectedLevel = levels.level_12
    width = 20

def SetupGuide(): #Initially function name was "UserInterface".

    #Level Selection
    inp_ = checkinp("Level Selection: Enter a number from 9 to 20:", lambda x: x.isdigit() and int(x) > 8 and int(x) < 21)
    selectedLevel = levels[eval("levels.level_" + inp_)]


    #For loop to print each list item in order for the user to see.
    for i in selectedLevel:
        print(str(i+". ") + selectedLevel[i])

    inp_ = 0    

    #Word selection
    inp_ = checkinp("Word Selection: Enter a number from 0 to" + str(len(selectedLevel)), lambda x: x.isdigit() and int(x) > 0 and int(x) < len(selectedLevel))
    selectedIndex = inp_
    #CHECK BOUNDARIES CAUSE I CAN'T THINK.
    
    #Amount of words to type
    inp_ = checkinp("Word amount selection: Enter any number that suits you.", lambda x: x.isdigit() and int(x) > 0)
    width = inp_


    #depth = int(input("Depth (0): ")) # remove text depth altogether?
    #Not very easy to keep track of word count with depth.
    
    #print("In total, you will be typing " + str(width * depth) + "words.") <<<That is pretty bad.
    
    return #MAY NEED TO RETURN SOME VALUES. WILL BE BACK TO THIS.
def counter():
    print(prompt)
    input(">>> Press ENTER to begin.")
    begin_time = time()
    inp = input("\n")
    end_time = time()
    final_time = (end_time - begin_time) / 60
    return final_time, inp

def wpm(time, line):
    # words = line.split()
    words = sum([len(word) for word in line.split()]) / 5
    words_per_m = words / time
    # word_length = len(words)
    # words_per_m = word_length / time
    return 
    #The wpm calculation should be
    #better now thanks to LeSirH.

def wordcheck(inp):
    #No idea if this works correctly but it should.
    #May not be a necessary function for the 100WPM+ gang however.
    prompts = prompt.split()
    inputs = inp.split()
    errorcount = 0
    idx = 0
    for inp in inputs:
        if inp != prompts[idx]:
            errorcount += 1
            if inp == prompts[idx + 1]:
                idx += 2
            elif inp != prompts[idx - 1]:
                idx += 1
        else:
            idx += 1      
    words_left = len(prompts) - len(inputs)
    correct = float(len(prompts)) - float(errorcount)
    percentage = (((float(correct) / float(len(prompts))) - float(words_left) / float(len(prompts))) * 100)
    return percentage

#Initialisation
choice = 0
percentager = 0

initialPrompt = ""
exit = False
while exit == False:
    choice = checkinp("Menu selection:\nPress 1 - Setup & guide.\nPress 2 - Skip setup. (Use default settings)\nPress 3 - Exit.", lambda x: x.isdigit() and int(x) > 0 and int(x) < 4)
    if choice == 1:
        userInterface()
    elif choice == 2:
        setupGuide()
    #elif choice == 3:
        #<Random word mode?>
    elif choice == 3:
        exit
        
    for i in range(0,depth):
        initialPrompt = initialPrompt+"\n"+width*(str(selectedLevel[selectedIndex])+" ")
    prompt = initialPrompt

    tm, line = counter()
    tm = round(tm, 2)
    words_per_minute = wpm(tm, line)
    #words_per_minute = round(words_per_minute, 2)
    print("You total time was:", tm ,"minutes")
    print("with an average of:", words_per_minute ,"words per minute")
    percentage = wordcheck(line)
    percentager = round(percentage, 2)
    print("with an accuracy of:", percentager ,"accuracy")
