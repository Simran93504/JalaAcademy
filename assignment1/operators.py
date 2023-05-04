print("*****************This program will let you know the use of operators in python *****************")


def arithmetic(a,b):
    print("**************** Function for arithmetic operators(+,-,*,/) **************** \n \n")
    print("Addition of two numbers is:",a+b)
    print("Subtraction of two numbers is:",a-b)
    print("Multiplication of two numbers is:",a*b)
    print("Division of two numbers is:",a/b)
    print("Modulus of two numbers is:",a%b)
    print("Exponent of two numbers is:",a**b)
    print("Floor division of two numbers is:",a//b)
    print("\n \n")


def increment_decrement(a,b):
    print("**************** method for increment and decrement operators(++, --) **************** \n \n")
    print("Increment of a is:",a+1)
    print("Decrement of b is:",b-1)
    print("\n \n")


def equal(a,b):
    
    print("**************** program to find the two numbers equal or not ****************")
    print("\n \n")
    if(a==b):
        print("a is equal to b")
    else:
        print("a is not equal to b")
    print("\n \n")    


def relational(a,b):
    print("****************** Program for relational operators (<,<==, >, >==) ******************")
    print("\n \n")
    if(a<b):
        print("a is less than b")
    elif(a<=b):
        print("a is less than or equal to b")
    elif(a>b):
        print("a is greater than b")
    elif(a>=b):
        print("a is greater than or equal to b")
    else:
        print("a and b are not equal")
    print("\n \n")    


def smaller_larger(a,b):
    print("********************Print the smaller and larger number between a and b*******************")
    print("\n \n")
    if(a<b):
        print("a is smaller than b")
    elif(a>b):
        print("a is greater than b")
    else:
        print("a and b are equal")
    print("\n \n")
        
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
arithmetic(a,b)
increment_decrement(a,b)
equal(a,b)
relational(a,b)
smaller_larger(a,b)


