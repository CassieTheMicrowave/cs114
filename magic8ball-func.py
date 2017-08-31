# Make a program based on the magic8ball.py program from Chapter 4 of your text.
#Have the program ask the user a question and based on their response determine which list of messages to pull from.
#(hint: use the len() function on their input)
#Save your program as magic8ball2.py


#9 responces user will get one of 9 differnt fortunes


from random import randint



def prompt_for_question():
    return int(input('This is a magic computer game. Why? Because there is no ball or eights. So anyways whats your name.'))


#def greeting():
    #return 'Hello, ' + name
def get_random():
    randnum = randint(1,10)
    return randnum

def awnsers(randnum):
    awnser = 0
    if randnum == 1:
        awnser = 'Nope, '
    elif randnum == 2:
        awnser = 'Yep, '
    elif randnum == 3 :
        awnser = 'Mabey.. I dont know Im a program, '
    elif randnum == 4:
        awnser = 'Does not look good... '
    elif randnum == 5:
        awnser = 'Like that would ever happen haha, '
    elif randnum == 6:
        awnser = 'I dont feel like it, ask a real magic eight ball, '
    elif randnum == 7:
        awnser = 'Looks like a possibility, '
    elif randnum == 8:
        awnser = 'Looks like it might happen, Jk no its never happening, '
    elif randnum == 9:
        awnser = 'Go away, '
    return awnser

def main():

    name = input('What is Your Name?')
    print("hi", name, "think of a question...")
    print("Here is your fortune:")
    randnum = get_random()
    fortune = awnsers(randnum)
    print(fortune)




main ()
