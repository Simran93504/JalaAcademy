print(" program to find the prime or not")

a = int(input("Enter the number: "))
if(a>1):
    b=2
    while(b!=a):
        if(a%b==0):
            print("The number is not prime")
            break
        b=b+1
    else:
        print("The number is prime")