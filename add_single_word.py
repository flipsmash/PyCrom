import warnings
warnings.filterwarnings("ignore")
from PyDictionary import PyDictionary
import json

dictionary=PyDictionary()
i=0
while i != -1:
    with open('definitions.txt') as json_data:
        d = json.load(json_data)
    i = input("Enter the word you want added: ")
    dict = str(dictionary.meaning(i))
    if dict == "None":
        print("There was no definition for {} in WordNet.".format(i))
        nd = input("Please enter the definition here:")
        d[i]=nd
    else:
        nd = dictionary.meaning(i)
        print("The WordNet definition is ", nd)
        d[i]=nd
    with open('definitions.txt','w') as f:
        json.dump(d,f)
    
        
    

    
    
