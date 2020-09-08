# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 13:08:04 2020

@author: Hrushabh Kotwal
"""
import os
npath = os.path.dirname(os.path.abspath(__file__))
import json
import difflib
from difflib import get_close_matches
def printDef(pmaterial):
    print("Meaning:")
    print(pmaterial + "\n")

def recheck(rword):  # Taking care of case sensitive words
    if rword.title() in dataDictionary:
        return(rword.title())
    elif rword.lower() in dataDictionary:
        return(rword.lower())
    elif rword.upper() in dataDictionary:
        return(rword.upper())
    else:
        global flag
        flag = 4

def findDefinition(word):
    global flag
    wflag = "True"
    nflag = "True"
    if word in dataDictionary:
        printDef(dataDictionary[word])
    else:

        result = recheck(word)
        if flag == 4:
            tlist = get_close_matches(word,dataDictionary.keys())
            if not tlist:
                print("The word that you have entered is incorrect.\nPlease recheck...")
            else:
                while wflag =="True":
                    YorN = input("Did you mean '"+ tlist[0] +"'\nEnter Y for Yes or Enter N for No: ")
                    if YorN == "Y" or YorN =="y":
                        printDef(dataDictionary[tlist[0]])
                        wflag = "False"
                    elif YorN == "N" or YorN =="n":
                        print("The word that you have entered is incorrect.\nPlease recheck...")
                        wflag = "False"
                    else:
                        print("\nPlease enter Y or N")
                        wflag = "True"
        else:
            YorN = input("Did you mean '"+ result +"'\nEnter Y for Yes or Enter N for No: ")
            if YorN == "Y" or YorN =="y":
                printDef(dataDictionary[result])
            else:
                print("The word that you have entered is incorrect.\nPlease recheck...")
    while nflag == "True":
        YorN = input("Do you wish to search another word ? \nPlease enter Y for Yes or N for No: ")
        if YorN == "Y" or YorN =="y":
            return(YorN)
            nflag = "False"
        elif YorN == "N" or YorN =="n":
            return(YorN)
        else:
            print("\nPlease enter Y or N")
            nflag = "True"
flag = 1
exitFlag = "False"
wildcard = "True"
dataDictionary  = dict()
dataDictionary  = json.load(open(npath + "\Dictionary-Advanced.json"))
while exitFlag =="False":
    toContinue = findDefinition(input("Enter the word for its definition: "))
    if toContinue == "N" or toContinue == "n":
        exitFlag = "True"
    elif toContinue =="Y" or toContinue == "y":
        nflag = "False"
input("Press enter to exit")
         
