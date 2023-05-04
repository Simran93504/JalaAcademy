print("program to find Armstrong number or not.")

a= int(input("Enter the number: "))
if(a>0):
    b=a
    c=0
    while(b!=0):
        d=b%10
        c=c+(d*d*d)
        b=b//10
    if(c==a):
        print("The number is Armstrong number")
    else:
        print("The number is not Armstrong number")