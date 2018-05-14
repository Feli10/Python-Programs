from random import randint
print('Ghost Game')
feelingBrave = True
score = 0
while feelingBrave:
    ghostDoor = randint(1,3)
    print('''Three doors ahead...
A ghost behind one...
Which door do you open?
''')
    door = int(input('1, 2, or 3?'))
    if door == ghostDoor:
        print('GHOST!')
        feelingBrave = False
    else:
        print('''No ghost!
You enter the next room...
''')
        score += 1
print('''Run away!
Game Over!
You scored''',score)


        
    
    
    
    
    
    


