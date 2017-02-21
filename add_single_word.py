import warnings
warnings.filterwarnings("ignore")
from PyDictionary import PyDictionary
import json

dictionary=PyDictionary()
i=0
while i != -1:
    i = input("Enter the word you want added: ")
    dict = str(dictionary.meaning(i))
    if dict == "None":
        print("There was no definition for {} in WordNet.".format(i))
    else:
        print("The WordNet definition is ", dictionary.meaning(i))

    
        
    

    
    
