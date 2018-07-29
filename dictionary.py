import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        answer = input( "Did you mean %s instead? type Y or N " % get_close_matches(word, data.keys())[0])
        if answer == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif answer == "N":
            return "Try again"
        else:
            return "I don't understnad your entry. type Y or N "
    else:
         return "The word does not exist."

while (True):
    word = input("Enter word: ")
    output = translate(word)
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)
