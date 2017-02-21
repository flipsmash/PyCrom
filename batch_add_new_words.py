from PyDictionary import PyDictionary
import json
dictionary=PyDictionary()
fo1 = open("new_words.txt", 'r')
lines_list = fo1.read().splitlines()
dicdic={}
undefs = []

for s in lines_list:
    word = str(s.upper())
    definition = str(dictionary.meaning(s))
    
    if definition == "None":
        undefs.append(word)
    else: dicdic[word] = definition

json.dump(dicdic, open("definitions.txt",'a'))
fo1.close()
fo2 = open('new_words.txt','w')
fo2.write('\n'.join(str(line) for line in undefs))
fo2.close()
print (undefs)
