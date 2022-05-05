'''
Improved by Presto-Creator

Based off Navendra Jha's Booth Algorithm Calculator
https://github.com/navi25
'''

import sys

def toBinary(n, l=8):
    return ("{0:0%db}" %l).format(n)

def toInt(b):
    return int(b,2)

z = 8

def flipBit(a):
    a = toBinary(a)
    b = ""
    for w in a:
        if w == '1':
            w = '0'
        else:
            w = '1'
        b += w
    return b

def twosComplement(b):
    w = flipBit(b)
    one = toBinary(1)
    a = addBinary(w, one)
    a = a[-8:]
    return a

def addBinary(a, b, l=8):
    return toBinary(int(a, 2) + int(b, 2))


def rightmostBit(a):
    return a[len(a)-1:]

def shiftRight(A):
    A = toInt(A)
    b = toBinary(A >> 1, 16)
    return b


def multiply(a,b):
    A = toBinary(0)
    B = ""
    q=""
    B_Comp = ""

    if(a < 0):  #For Negative Number
        a *= -1
        B = twosComplement(a)
        B_Comp = toBinary(a)
    else:
        B = toBinary(a)
        B_Comp = twosComplement(a)

    if(b<0):  #For Negative Number
        b *= -1
        q = twosComplement(b)
    else:
        q = toBinary(b)


    q1 = '0'

    
    count = z
    step = 1

    while(count>0):
        q0 = rightmostBit(q)
        print(step,end="\t\t\t|")

        #DO NOTHING SINCE 00 OR 11 ENDING
        if ((q0 == '0') and (q1 == '0')) or ((q0 == '1') and (q1 == '1')):
            print("No Operation\t\t|",end=" ")
            print(str(toBinary(a)),end="\t\t|")
            print(str(toBinary(b)),end=" ")
            print(q1)
            c = A + q + q1
            c = shiftRight(c)
            c = A[0] + c
            A = c[:z]
            q = c[z:2*z]
            q1 = c[len(c)-1]
            print("\t\t\t|Shift Right\t\t|", end=" ")
            print(str(toBinary(a)),end="\t\t|")
            print(str(q),end=" ")
            print(q1)
            
        #-=MCAND BECAUSE 10 ENDING
        elif (q0 == '1') and (q1 == '0'):
            print("prod=prod-Mcand\t|",end=" ")
            print(str(toBinary(a)),end="\t\t|")
            A = addBinary(A, B_Comp, 8)
            A = A[-8:]
            c = A + q + q1
            print(str(c),end=" ")
            print(q1)
            c = shiftRight(c)
            c = A[0] + c
            A = c[:z]
            q = c[z:2*z]
            q1 = c[len(c)-1]
            print("\t\t\t|Shift Right\t\t|", end=" ")
            print(str(toBinary(a)),end="\t\t|")
            print(str(q),end=" ")
            print(q1)


        #+=MCAND BECAUSE 01 ENDING
        elif (q0 == '0') and (q1 == '1'):
            print("prod=prod+Mcand\t|",end=" ")
            print(str(toBinary(a)),end="\t\t|")
            A = addBinary(A, B, 8)
            A = A[-8:]
            c = A + q + q1
            print(str(c),end=" ")
            print(q1)
            c = shiftRight(c)
            c = A[0] + c
            A = c[:z]
            q = c[z:2*z]
            q1 = c[len(c)-1]
            print("\t\t\t|Shift Right\t\t|", end=" ")
            print(str(toBinary(a)),end="\t\t|")
            print(str(q),end=" ")
            print(q1)

        
        count-=1
        step+=1
        print("\n___________________________________________________________________")

    return A+q

def printResult(a):
    res = ""
    if a[0] == '1':
        i = toInt(a)
        b = flipBit(i)
        one = toBinary(1)
        res = addBinary(b, one)
    else:
        res = a

    value = toInt(res)
    if a[0] == '1':
        value*=-1

    print("which is " , value)


def calculateBooth(a,b):
    c = (multiply(a,b))
    print("The final product is: ", c, end=" ")
    printResult(c)

def main():
    
    s = int(input("Enter the multiplicand (between -127 and 127): "))
    t = int(input("Enter the multiplier (between -127 and 127): "))

    if (s > 127 or s < -127):
        sys.exit("Input is not correct, exiting!")
        
    elif (t > 127 or t < -127):
        sys.exit("Input is not correct, will exit!")
     

    a = ""
    b = ""
        
    a = s
    b = t
    
    #print the first statement
    print("Iteration\t| Step\t\t\t| Multiplicand\t | Product")
    print("___________________________________________________________________")
    
    #INTIIALIZE
    print("0\t\t\t| Initialize\t\t|",end=" ")
    print(toBinary(a), end=" ")
    print("\t\t| ",end=" ")
    print(toBinary(b), end=" ")
    print(toBinary(b)[-1], end=" ")
    
    #STUFF HERE
    print("\n___________________________________________________________________")


    calculateBooth(a,b)


if __name__ == "__main__":
   main()


















