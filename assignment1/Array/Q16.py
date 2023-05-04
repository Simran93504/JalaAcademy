print("Write a method to verify if the array contains two specified elements(12,23)")
n=int(input("Enter the size of array: "))
arr=[]
print("Enter the elements of array: ")
for i in range(n):
    arr.append(int(input()))
if 12 in arr and 23 in arr:
    print("True")
else:
    print("False")
print()
