import json
import random
from random import shuffle
with open('definitions.txt') as json_data:
    d = json.load(json_data)
q=1
correct = 0
incorrect = 0

needs_work = []

while 1:
    rand_word = random.choice(list(d.keys()))
    print("Word: ", rand_word)
    aa = str(d[rand_word])
    ba = str(d[random.choice(list(d.keys()))])
    ca = str(d[random.choice(list(d.keys()))])
    da = str(d[random.choice(list(d.keys()))])
    ans_choice = [aa,ba,ca,da]

    shuffle(ans_choice)
    ans_choice.append("No idea!")
    i=0

    for e in ans_choice:
        letter = ["A. ", "B. ", "C. ", "D. ", "E. "]
        print (str(letter[i]),e)
        i+=1

    la = {"A":0,"B":1,"C":2,"D":3, "E":4}
    answer_input = input("\nAnswer: ").upper()

    if ans_choice[la[answer_input]] == d[rand_word]:
        print ("\nCORRECT!")
        correct+=1
    else:
        print ("\nWRONG.  The correct definition is:")
        print (d[rand_word])
        incorrect+=1
        needs_work.append(rand_word)

    q = input()
    if q == "-1": break
correct_pct = str(round(correct/(correct+incorrect)*100,1))
print("Your percentage correct was ", correct_pct, ".")
print("Words you got wrong include the following",needs_work)
