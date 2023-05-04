print("Write a method to remove duplicate elements from an array")
n=int(input("Enter the size of array: "))
arr=[]
print("Enter the elements of array: ")
for i in range(n):
    arr.append(int(input()))
print("Array after removing duplicate elements: ")
for i in arr:
    if arr.count(i)>1:
        arr.remove(i)
print(arr)
print()
