from time import time
import levels
i, initialPrompt = 0, ""

#I was too lazy to create a simple user interface, so just change
#the four variables below to navigate through the word levels:

selectedIndex = 0
selectedLevel = levels.level_9
width = 3
depth = 4

#You are of course allowed to modify the code however you want, and you may
#even want to do that since it does require some fiddling at times using this
#program.

#I personally find depth = 1 and width > 1, to be best.

for i in range(0,depth):
    initialPrompt = initialPrompt+"\n"+width*(str(selectedLevel[selectedIndex])+" ")
prompt = initialPrompt

def counter():
    # i = 0 
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

tm, line = counter()
tm = round(tm, 2)
words_per_minute = wpm(tm, line)
words_per_minute = round(words_per_minute, 2)
print("You total time was:", tm ,"minutes")
print("with an average of:", words_per_minute ,"words per minute")
percentage = wordcheck(line)
percentager = round(percentage, 2)
print("with an accuracy of:", percentager ,"accuracy")
