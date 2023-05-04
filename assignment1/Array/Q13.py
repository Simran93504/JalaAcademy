print("Write a method to find the second largest number in an array")
n=int(input("Enter the size of array: "))
arr=[]
print("Enter the elements of array: ")
for i in range(n):
    arr.append(int(input()))
arr.sort()
print("Second largest element is: ",arr[-2])
print()