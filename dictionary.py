import json
import difflib
from difflib import SequenceMatcher 
from difflib import get_close_matches
data = json.load(open("/home/mente/Documents/Mente/Codes/pythonprojects/advanced projects/Interactive Dictionary/076 data.json"))


def translate(w):
    w = w.lower()
    if w in data:
        return data[w] 
    elif len(get_close_matches(w, data.keys())) > 0:
        yesNo= input("Did you mean %s instead? Enter Y if yes or N if no: " % get_close_matches(w, data.keys())[0])
        if yesNo == 'Y':
            return data[get_close_matches(w, data.keys())[0]]
        
        elif yesNo == 'N':
            return "The word you are looking for doesn't exist"
        else:
            return "You entered unexpected letter. please try again."
  
    else:
        return "The word you have entered is not exist, please try again other word"

word = input("Enter a word to be translated: ")

output = (translate(word))
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)


#print(SequenceMatcher(None,"Rainn","rain").ratio()) is a library that matches a squence of the words 

""" 
    data.keys()
    print(get_close_matches("rainn",data.keys()))  :- get close matches is used to get the closest match of the given word

"""
 
 



















