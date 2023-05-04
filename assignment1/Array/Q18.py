print("Write a program to remove the duplicate elements and return the new array")

n=int(input("Enter the size of array: "))
arr=[]
print("Enter the elements of array: ")
for i in range(n):
    arr.append(int(input()))
print("Array after removing duplicate elements: ")
arr1=[]
for i in arr:
    if i not in arr1:
        arr1.append(i)
print(arr1)
print()
