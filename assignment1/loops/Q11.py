print(" Program to check whether a number is EVEN or ODD using switch")

a= int(input("Enter the number: "))
switch = {
    a%2==0: "The number is even",
    a%2!=0: "The number is odd"
}
print(switch.get(True))