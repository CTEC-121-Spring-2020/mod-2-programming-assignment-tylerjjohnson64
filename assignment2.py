"""
CTEC 121
Tyler Johnson
assignment 2
print statements 
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""
from math import *
def main():
    
    # problem 1
    aFloat = 12.65
    anInt = 12
    aString = ("This is a string.") 
    print()
    print(anInt)   
    print()
    print(aFloat)
    print()
    print(aString)
    print()
    print("This is me demonstrating my print skills."" I will print the string I declared previously:",aString,"Isn't that cool! ")

    #problem 2 
    print()
    print("I'm going to use end and sep commands in my print statement!",end="\n")
    print("Coded "'4','28','2020',sep="-")

    #problem 3 
    print()
    print('\t''\"' '/' " Using escapes. " '/' '\"')
    
    #problem 4 
    print()
    iString=input("Enter a string: ")
    iInt= int(input("Enter an integer: "))      #will not accept real numbers
    iFloat=float(input("Enter a float: "))
    X=20
    #expression=eval(X+1)
    print()
    print("This is your string:",iString,)
    print("This is your integer:" ,iInt,)
    print("This is your float:" ,iFloat,)
    print("X=",X)
    print("This is your X increased by 1:",eval("X+1"))
    print()
    #problem 5 
    a, b = eval(input("Enter two numbers seperated by a comma: "))
    print(a, b)
    print()
    c, d = input("Provide two values seperated by a space: ").split()
    print(c,d)
    print()

    #problem 6 
    print('five divided by two')
    print(5/2)
    print()
    print("remainder 5 divided by two")
    print(5%2)
    print()

    #problem 7 
    print('List')
    for i in [1,2,3,4,5]:
        print(i)

    print()
    print('Range')
    for i in range(4):
        print(i)
    print()
    print('By 5')
    for i in range(11,41,5):
        print(i)

    print()
    
    #problem 8 
    print("value of pi")
    print(pi)
    print("square root of 4")
    print(sqrt(4))
    print('ceiling 3.2')
    print(ceil(3.2))
    print('floor 4.2')
    print(floor(4.2))
    print('two squared')
    print(2**2)
    print('two cubed')
    print(2**3)
    print()
    
    #problem 9 
    sum = 0
    square = 0
    for i in range(5):
        inputValue = eval(input("Enter a number: "))
        sum = sum + inputValue
        square = square + (inputValue**2)
    print("The sum of inputs is:", sum)    
    print()
    print("The sum of squares of inputs is:", square)
    print()

    #bonus
    r = (eval(input('Enter a value of r: ')))
    V = (float((4.0 * (pi*(r**3)))/3.0))    
    print(V)  
    print()
   
    
    r = (eval(input('Enter a value: ')))  
    area = (float(4*(pi*(r**2))))
    print()
    print(area)
    print()
   
    y1,y2 = eval(input("enter Y values Y1 and Y2 seperated by comma: "))
    x1,x2 = eval(input("enter x values X1 and X2 seperated by comma: "))
    slope = (y2-y1)/(x2-x1)
    print("slope =",slope)
    print()
    
    a,b,c = eval(input("enter 3 values seperated by a comma: "))
    s = ((a+b+c)/2)
    print(s)
    print()
    
    #attempted but not complete
    s=(1,2,3)
    a,b,c = eval(input('Enter three values seperated by commas: '))
    A= (sqrt(s*((s-a)*(s-b)*(s-c))))
    print(A)
main()