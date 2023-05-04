print(" program to palindrome or not.")
# for a string
string = input("Enter the string: ")
if(string == string[::-1]):
    print("The string is palindrome")
else:
    print("The string is not palindrome")
    
# for a number

num = int(input("Enter the number: "))
temp = num
rev=0
while(temp>0):
    a = temp%10
    rev = rev*10 + a
    temp //= 10
if(num == rev):
    print("The number is palindrome")
else:
    print("The number is not palindrome")
