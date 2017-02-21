from PyDictionary import PyDictionary
import json
dictionary=PyDictionary()
lines_list = open('vocab', 'r').read().splitlines()

dicdic={}
undefs = []

for s in lines_list:
    word = str(s.upper())
    definition = str(dictionary.meaning(s))
    
    if definition == "None":
        undefs.append(word)
    else: dicdic[word] = definition

json.dump(dicdic, open("definitions.txt",'w'))

print (undefs)
  
