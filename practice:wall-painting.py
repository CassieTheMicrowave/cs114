#All our friends are re-painting one wall of their rooms.
#hey want us to figure out how much it's going to cost.
#Assume one gallon of paint covers 400 square feet.
print ("What is the wall hieght?")
hieght = input()
print ("What is the wall width?")
width = input()
print ("How much is a gallon of paint coat?")
paint_amount = float(input())
print ("How many coats will you use?")
coats = input()
squarefeet = round(((int(hieght) * int(width)) * int(coats)) / 400)
print (float(squarefeet * int(paint_amount)))
