#Create a program that asks for a number in base-10 that's between 1 and 99
#then prints out the name of it in English.
#45 fourty-five
#11 eleven
#print ("If you give me a normal number between 1 and 99 I can wright it out")
#number = input()
def prompt_for_number():
    return int(input('If you give me a normal number between 1 and 99 I can wright it out: '))

def get_tens_digit(number):
    return number // 10

def get_ones_digit(number):
    return number % 10


def tens_digit_to_word(tens):
    if tens == 9:
        tens_word = 'ninety'
    elif tens == 8:
        tens_word = 'eighty'
    elif tens == 7:
        tens_word = 'seventy'
    elif tens == 6:
        tens_word = 'sixty'
    elif tens == 5:
        tens_word = 'fifty'
    elif tens == 4:
        tens_word = 'forty'
    elif tens == 3:
        tens_word = 'thirty'
    elif tens == 2:
        tens_word = 'twenty'
    #elif tens == 1:
        #tens_word = 'teen'
    else:
        tens_word = ' '
    return tens_word


def ones_digit_to_word(ones):
    if ones == 9:
        one_word = 'nine'
    elif ones == 8:
        one_word = 'eight'
    elif ones == 7:
        one_word = 'seven'
    elif ones == 6:
        one_word = 'six'
    elif ones == 5:
        one_word = 'five'
    elif ones == 4:
        one_word = 'four'
    elif ones == 3:
        one_word = 'three'
    elif ones == 2:
        one_word = 'two'
    elif ones == 1:
        one_word = 'one'
    else:
        one_word = 'zero'
    return one_word


def assemble_word_regular(tens, ones, tens_word, ones_word):
    if ones == 0:
        return tens_word
    elif tens == 0:
        return one_word
    else:
        return tens_word + '-' + ones_word
































#def assemble_word_regular():
    #if ones == 0:
    #    return tens_word
#    elif tens == 0:
    #    return ones_word
    #else:
        #return tens_word + '-' + ones_word



def assemble_word_irregular(tens, tens_word):
    if tens == 1:
        output = 'eleven'
    elif tens == 2:
        output = 'twelve'
    elif tens == 3:
        output = 'thirteen'
    else:
        output = one_word + 'teen'
    return output


def assemble_words(tens, ones, tens_word, ones_word):
    if tens == 1:
        output = assemble_word_irregular(ones, ones_word)
    else:
        output = assemble_word_regular(tens, ones, tens_word, ones_word)
    return output

def main():
    number = prompt_for_number()
    tens = get_tens_digit(number)
    ones = get_ones_digit(number)
    tens_word = tens_digit_to_word(tens)
    one_word = ones_digit_to_word(ones)
    output = assemble_words(tens, ones, tens_word, one_word)
    print(output)
#print()




main()
