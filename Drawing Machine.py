from turtle import *
def turtleController(do,val):
    if do == 'f':
        forward(val)
    elif do == 'b':
        backward(val)
    elif do == 'r':
        right(val)
    elif do == 'l':
        left(val)
    elif do == 'u':
        penup()
    elif do == 'd':
        pendown()
    elif do == 'n':
        reset()
    else:
        print('Unrecognized Command')

def stringArtist(program):
    cmdList = program.split('-')
    for command in cmdList:
        cmdLen = len(command)
        if cmdLen == 0:
            continue
        cmdType = command[0]
        num = 0
        if cmdLen > 1:
            numString = command[1:]
            num = int(numString)
        print(command)
        turtleController(cmdType,num)
instructions ='''
n = New Drawing
u/d = Pen up/down
f100 = Forward 100
b100 = Backwards 100
r90 = Right 90 degrees
f90 = Left 90 degrees
'''
screen = getscreen()
while True:
    window = screen.textinput('Drawing Machine',instructions)
    print(window)
    if window == None or window.upper() == 'END':
        break
    stringArtist(window)
    
    



    



    
    
    
