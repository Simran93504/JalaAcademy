print(" Write a function to get the difference of largest and smallest value")

n=int(input("Enter the size of array: "))
arr=[]
print("Enter the elements of array: ")
for i in range(n):
    arr.append(int(input()))
arr.sort()
print("Difference of largest and smallest value is: ",arr[-1]-arr[0])