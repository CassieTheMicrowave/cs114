#Create a program that asks for a number in base-10 that's between 1 and 99
#then prints out the name of it in English.
#45 fourty-five
#11 eleven
print ("If you give me a normal number between 1 and 99 I can wright it out")
#number = input()
number = int(input())

tens = number // 10
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
elif one == 9:
    one = 'nine'
elif one == 8:
    one = 'eight'
elif one == 7:
    one = 'seven'
elif one == 6:
    one = 'six'
elif one == 5:
    one = 'five'
elif one == 4:
    one = 'four'
elif one == 3:
    one = 'three'
elif one== 2:
    one = 'two'
elif one == 1:
    one = 'one'
else:
    print("Sorry cant do it.")
