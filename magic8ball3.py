import random
from time import sleep

print ("Think of a question, and the answer shall be given.... Mabey")
sleep(3)

answer = ['Nope',
'Yep',
'Maybe.. I dont know Im a program',
'Does not look good...',
'Like that would ever happen haha',
' dont feel like it, ask a real magic eight ball',
'Looks like a possibility',
'Looks like it might happen, Jk no its never happening',
'Go away',]

print(answer[random.randint(0, len(answer)-1)])
