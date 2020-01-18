from time import time
i, initialPrompt = 0, ""
level_20 =[ "abetalipoproteinemia","hyperlipoproteinemia",
            "semiautobiographical","internationalization",
            "compartmentalisation","uncharacteristically",
            "undiscriminatingness","counterrevolutionary",
            "unsubstantialization","overenthusiastically",
            "incontrovertibleness","disproportionateness",
            "counterdemonstration","unimpressionableness",
            "undiscriminativeness","indistinguishability",
            "counterrevolutionist","philosophicojuristic",
            "nonrepresentationist","intercommunicational",
            "magnetohydrodynamics","anthropomorphization" ]

level_19 =[ "auriculoventricular","contemporaneousness",
            "conventionalisation","conventionalization",
            "counterdemonstrator","counterintelligence",
            "counterproductively","countertransference",
            "dissatisfactoriness","electrocardiography",
            "individualistically","intellectualisation",
            "intellectualization","interchangeableness",
            "photodisintegration","pneumoencephalogram",
            "professionalisation","professionalization",
            "pseudohallucination","psychophysiological",
            "straightforwardness","unauthoritativeness",
            "uncommunicativeness","unsophisticatedness" ]

level_18 =[ "characteristically","transubstantiation",
            "oversimplification","anthropocentricity",
            "bioinstrumentation","discriminativeness",
            "intercommunication","overcapitalisation",
            "misrepresentaation","sentimentalization",
            "forethoughtfulness","counterintuitively",
            "discriminatingness","chemicoengineering",
            "unappreciativeness","unsatisfactoriness" ]

level_17 =[ "interdisciplinary","industrialization",
            "collaborativeness","industrialisation",
            "decriminalization","telecommunication",
            "demasculinisation","maladministration",
            "misrepresentation","misadministration",
            "contradistinction","hyperpigmentation",
            "misinterpretation","concentralization",
            "conceptualization","misidentification",
            "immunosuppression","heterogeneousness" ]

level_16 =[ "overcompensation","extraterrestrial",
            "misunderstanding","enthusiastically",
            "hydroelectricity","undifferentiated",
            "apprehensiveness","neurotransmitter",
            "reinterpretation","responsibilities",
            "characterisation","environmentalist",
            "counterbalancing","contraindication",
            "hyperventilation","simultaneousness" ]

level_15 =[ "procrastination","personification",
            "characteristics","desertification",
            "thermochemistry","congratulations",
            "interdependance","accomplishments",
            "acclimatisation","maneuverability",
            "rationalisation","syllabification",
            "mischievousness","discombobulated",
            "trustworthiness","insubordination",
            "excommunication","internalization",
            "misappreciation","confidentiality" ]
            
level_14 =[ "abrasivenesses","absolutenesses",
            "abstemiousness","abstractedness",
            "abstractionism","abstractionist",
            "abstractnesses","abstrusenesses",
            "acceleratingly","accelerometers",
            "acceptableness","accident-prone",
            "accidentalness","accommodations",
            "accompaniments","accomplishment",
            "accountability","accreditations",
            "acculturations","accumulatively" ]

level_13 =[ "approximately","automatically",
            "circumstances","collaboration",
            "communication","comprehensive",
            "configuration","consideration",
            "contributions","documentation",
            "entertainment","environmental",
            "functionality","international",
            "investigation","manufacturers",
            "manufacturing","opportunities",
            "organizations","participation",
            "professionals","relationships",
            "significantly","understanding",
            "unfortunately","accommodation",
            "administrator","alternatively",
            "championships","collaborative",
            "concentration","consciousness",
            "controversial","conversations",
            "corresponding","concatenation",
            "certification","determination" ]

            
level_12 =[ "additionally","applications",
            "architecture","availability",
            "capabilities","championship",
            "compensation","consequences",
            "construction","contemporary",
            "conversation","distribution",
            "expectations","improvements",
            "increasingly","installation",
            "institutions","instructions",
            "intelligence","introduction",
            "manufacturer","neighborhood",
            "organization","participants",
            "particularly","presentation",
            "professional","registration",
            "relationship","requirements",
            "specifically","successfully",
            "technologies","temperatures",
            "transactions","transmission" ]
            
level_11 =[ "accessories" "advertising",
            "alternative","application",
            "appointment","appropriate",
            "association","authorities",
            "certificate","combination",
            "comfortable","communicate",
            "communities","competition",
            "competitive","complicated",
            "connections","consumption",
            "corporation","demonstrate",
            "description","destination",
            "development","differences",
            "educational","effectively",
            "electricity","enforcement",
            "engineering","environment",
            "essentially","established",
            "experienced","experiences",
            "explanation","flexibility" ]
            
level_10 =[ "absolutely","accessible",
            "activities","additional",
            "affordable","apparently",
            "appearance","applicable",
            "applicants","appreciate",
            "assessment","assistance",
            "associated","atmosphere",
            "attractive","background",
            "basketball","businesses",
            "candidates","categories",
            "challenges","characters",
            "collection","commercial",
            "commission","commitment",
            "comparison","compatible",
            "completely","completion",
            "compliance","components",
            "conclusion","conditions",
            "conference","confidence" ]

level_9 =[ "abilities","according",
           "admission","advantage",
           "adventure","afternoon",
           "agreement","alongside",
           "announced","apartment",
           "attention","authority",
           "automatic","available",
           "awareness","basically",
           "batteries","beautiful",
           "beginning","breakfast",
           "brilliant","buildings",
           "candidate","carefully",
           "celebrate","certainly",
           "certified","challenge",
           "character","childhood",
           "chocolate","classroom",
           "collected","committed",
           "committee","community" ]

personal_favourites =[ "something", "everything", "throughout",
                       "without", "therefore", "although",
                       "alliteration", "intimate", "iniative",
                       "inanimate", "yourself", "right",
                       "righteous", "rollover", "mitigation",
                       "attentuation", "anonimity", "ambiguity",
                       "interference", "intercommunication"
                       "abbreviation", "arrangement" ]

#I was too lazy to create a simple user interface, so just change
#the four variables below to navigate through the word levels:

selectedIndex = 0
selectedLevel = level_9
width = 3
depth = 4

#You are of course allowed to modify the code however you want, and you may
#even want to do that since it does require some fiddling at times using this
#program.

#I personally find depth = 0 and width = anything, to be best.

for i in range(0,depth):
    initialPrompt = initialPrompt+"\n"+width*(str(selectedLevel[selectedIndex])+" ")
prompt = initialPrompt

def counter():
    i = 0 
    print(prompt)
    input(">>> Press ENTER to begin")
    begin_time = time()
    inp = input("\n")
    end_time = time()
    final_time = (end_time - begin_time) / 60

    return final_time, inp

def wpm(time, line):
    words = line.split()
    word_length = len(words)
    words_per_m = word_length / time
    #Discord people pointed out that this calculation is wrong.
    #Will change later, and may even add different website wpm
    #modes if for example, 10ff uses a different wpm formula from
    #typeracer.
    return words_per_m

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
