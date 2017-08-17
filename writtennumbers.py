#Create a program that asks for a number in base-10 that's between 1 and 99
#then prints out the name of it in English.
#45 fourty-five
#11 eleven
#print ("If you give me a normal number between 1 and 99 I can wright it out")
#number = input()
numbers = int(input('If you give me a normal number between 1 and 99 I can wright it out: '))

tens = numbers // 10
ones = numbers % 10

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
elif tens == 1:
    tens_word = 'teen'
else:
    tens_word = ' '
#return tens_word

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



if tens == 0:
    output = one_word
elif tens == 1:
    if ones == 1:
        output = 'eleven'
    elif ones == 2:
        output = 'twelve'
    elif ones == 3:
        output = 'thirteen'
    else:
        output = one_word + 'teen'
else:
    output = tens_word + '-' + one_word

print(output)
