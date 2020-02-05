#I know that the inp_ and _inp variables are quite unnecessary, but I just find it more comfortable this way.
#Do what you want with them.
from time import time
import levels

#Initialisation
selectedIndex = 0
selectedLevel = levels
width = 0
depth = 0

def checkinp(disp, errlambda) :
    inp = ""
    while True :
        if errlambda(input(disp)):
            #print("Proceeding...") No need to tell the user imo
            return inp
        else:
            print("<!> Incorrect Input <!>")

def defaultValues():
    selectedIndex = 5
    selectedLevel = levels.level_12
    width = 20
    return selectedIndex, selectedLevel, width

def setupGuide():
    #Level Selection
    inp_ = checkinp("Level Selection: Enter a number from 9 to 20:", lambda x: x.isdigit() and int(x) > 8 and int(x) < 21)
    selectedLevel = levels[eval("levels.level_" + inp_)]
    #For loop to print each list item in order for the user to see.
    for i in selectedLevel:
        print(str(i+". ") + selectedLevel[i])
    inp_ = 0    
    #Word selection
    #Fixed by casting to int
    selectedIndex = int(checkinp("Word Selection: Enter a number from 0 to {0}".format(len(selectedLevel)), lambda x: x.isdigit() and int(x) > 0 and int(x) < len(selectedLevel)))
    #NEED TO TEST BOUNDARIES CAUSE I CAN'T THINK.
    #Amount of words to type
    inp_ = checkinp("Word amount selection: Enter any number that suits you.", lambda x: x.isdigit() and int(x) > 0)
    width = inp_


    #depth = int(input("Depth (0): ")) # remove text depth altogether?
    #Not very easy to keep track of word count with depth included.
    
    #print("In total, you will be typing " + str(width * depth) + "words.") <<<That is pretty bad lol
    return selectedLevel, selectedIndex, width
def counter():
    print(prompt)
    input(">>> Press ENTER to begin.")
    begin_time = time()
    _inp = input("\n")
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
    #These wpm calculations should be
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

choice = checkinp("Menu selection:\nPress 1 - Setup & guide.\nPress 2 - Skip setup. (Use default settings)\nPress 3 - Exit.", lambda x: x.isdigit() and int(x) > 0 and int(x) < 4)
if choice == 1:
    setupGuide()
elif choice == 2:
    defaultValues()
    #ERROR?
#elif choice == 3:
    #<Random word mode?>
elif choice == 3:
    
    exit
#User will have the option to quickly restart the track they just practised. Will implement later.

initialPrompt = selectedLevel[selectedIndex] #ERROR HERE?
prompt = initialPrompt
#I am aware that initialPrompt variable is unnecessary. 

tm, line = counter()
tm = round(tm, 2)
words_per_minute = wpm(tm, line)
#words_per_minute = round(words_per_minute, 2)
print("You total time was:", tm ,"minutes")
print("with an average of:", words_per_minute ,"words per minute")
percentage = wordcheck(line)
percentager = round(percentage, 2)
print("with an accuracy of:", percentager ,"accuracy")
