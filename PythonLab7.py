x = 1
while(x < 300):
    print x
    x = x + 2
    
myList = [1,2,3,4,5,6,7,8,9,10]
index = 0
while(index < len(myList)):
    print myList[index]
    index = index + 1
    
import random
random = random.randint(0,50)
userInput = int(raw_input())
while(userInput != random):
    if userInput > random:
        print 'too big'
        userInput = int(raw_input())
    else:
        print 'too small'
        userInput = int(raw_input())
print 'you win'