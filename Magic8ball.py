# Make a program based on the magic8ball.py program from Chapter 4 of your text.
#Have the program ask the user a question and based on their response determine which list of messages to pull from.
#(hint: use the len() function on their input)
#Save your program as magic8ball2.py


#9 responces user will get one of 9 differnt fortunes

from random import randint

print ("This is a magic computer game. Why? Because there is no ball or eights. So anyways whats your name.")
name = input()

r = randint(1,10)

if r==1:
    print ("Nope, ")
elif r==2:
    print ("Yep, ")
elif r==3 :
    print ("Mabey.. I dont know Im a program, ")
elif r==4:
    print ("Does not look good... ")
elif r==5:
    print ("Like that would ever happen haha, ")
elif r==6:
    print ("I dont feel like it, ask a real magic eight ball, ")
elif r==7:
    print ("Looks like a possibility, ")
elif r==8:
    print ("Looks like it might happen, Jk no its never happening, ")
elif r==9:
    print ("Go away, ")


print (name)
