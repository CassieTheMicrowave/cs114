#The NOUN jumped over the ADJ NOUN.
from time import sleep
print ("We are going to play madlib. Yay")
sleep(1)
print ("Can you give me a Noun?")
Noun1 = input()
print ("Can you give me a Adjective?")
adjective = input()
print ("Can you give me one more Noun?")
Noun2 = input()
print ("The " + (Noun1) + " jumped over the " + (adjective) + " " + (Noun2) + ".")
sleep(1)
print ("Want to play another one?")
awnser = input()
if awnser == 'yes' :
    print ("Yay. Can you give me a noun?")
    noun3 = input()
    print ("Can you give me another noun?")
    noun4 = input()
    print("Can you give me an adjative?")
    adjective2 = input()
    #The noun made the noun adjective
    print("The " + (noun3) + " made the " + (noun4) + " " + (adjective2) + ".")
    sleep(1)
    print ("Bye bye. See you later.")

elif awnser == 'no' : print ("Well I guess I will just cry in this corner... Im sooooo lonely.")
