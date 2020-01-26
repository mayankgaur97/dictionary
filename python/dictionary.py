import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches
data = json.load(open("files/data.json"))

while True :
    print("welcome to makk dictionary")

    def return_word(w):
        w=w.casefold()
        if w in data:
            return data[w]
        elif w.title()in data :
            return data[w.title()]
        elif w.upper() in data:
            return data[w.upper()]
        elif len(get_close_matches(w,data.keys()))>0 :
            respnonse = input("did you mean %s instead Enter Y  for yess or N  for no  :" % get_close_matches(w,data.keys())[0])
            if respnonse.casefold() == "y":
                return data[get_close_matches(w,data.keys())[0]]
            elif respnonse.casefold() == "n":
                return "sorry could'nt find world"
            else:
                return "we did'nt get your entry"
                
        else :
            return "word does not exist"

    word=input("enter the word : ")
    output = (return_word(word))

    if type(output)== str:
        print (output)
    else :
        for item in output:
            print (item)
        
    again=input("Do you want to enter more word. Enter Y  for yess or N  for no : ")
    if again =="Y"  :
        continue
    else :
        break
