#Code not tested/simplified (yet) after multiple changes made.
from time import time
import levels
initialPrompt = ""

#User Interface
selectedIndex = 0
selectedLevel = levels
width = 0
depth = 0

def defaultValues():
    selectedIndex = 5
    selectedLevel = levels.level_12
    width = 20
    depth = 1

def userInterface():
    
   #These three similar loops are just error preventions. Will merge them/make them smaller later.
#You can tell i'm not too good at this.
#Got some code to make them better.
    Pass = False
    while Pass == False:
        try:
            selectedLevel = eval("levels.level_" + input("Choose a level between 9 and 20: "))
            Pass = False
        except:
            print("Invalid input type")
            Pass = True
        if not inp in range(9,21):
            if Pass == False:
                print("Number out of range")
            else:
                Pass = False
        else:
            Pass = True
    selectedLevel = levels[selectedLevel]

    #For loop to print each list item in order
    for i in selectedLevel:
        print(str(i+". ") + selectedLevel[i]))
        
#depth = int(input("Depth (0): ")) # remove depth altogether?

    Pass = False
    while Pass == False:
        try:
            selectedIndex = input("Enter the number of the word you want to type:")
            print("The available range is: 0 to",len(selectedLevel))
            Pass = False
        except:
            print("Invalid input type")
            Pass = True
        if not inp in range(9,21):
            if Pass == False:
                print("Number out of range")
            else:
                Pass = False
        else:
            Pass = True
    
    #Text display
    Pass = False
    while Pass == False:
        try:
            width = int(input("Width (3): "))
            print("The available range is: 0 to",len(selectedLevel))
            Pass = False
        except:
            print("Invalid input type")
            Pass = True
        if not inp in range(0, len(selectedLevel)+1):
            if Pass == False:
                print("Number out of range")
            else:
                Pass = False
        else:
            Pass = True
    #print("In total, you will be typing " + str(width * depth) + "words.")

def counter():
    print(prompt)
    input(">>> Press ENTER to begin")
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
    
    #The wpm calculations should be better now thanks to 
    #the one and only contributor.
    return 

def wordcheck(inp):
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

percentager = 0
exit = False
choice = 0
while exit == False:
     
    choice = input("Choose either:\n1. Setup & guide.\n2. Skip setup. (Use default settings)\n3. Exit."))
    while not isinstance(choice, int):
            print("<!> Has to be a number <!>")
            choice = int(input("Choose either:\n1. Setup guide.\n2. Skip setup. (Use default settings)\n3. Exit."))
    while not choice in range(1,4):
        print("<!> Has to be a number between 1 and 3 <!>")
        choice = int(input("Choose either:\n1. Setup guide.\n2. Skip setup. (Use default settings)\n3. Exit."))
        
    if choice == 1:
        userInterface()
    elif choice == 2:
        defaultValues()
    elif choice == 3:
        exit
    i = 0
    
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
