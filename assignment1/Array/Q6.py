print("Write a function to copy an array to another array")

n=int(input("Enter number of elements: "))
arr=[]
for i in range(0,n):
    ele=int(input("Enter elements:"))
    arr.append(ele)
print("Array is:",arr)
arr1=[]
for i in range(0,n):
    arr1.append(arr[i])
print("Copied array is:",arr1)
print("\n \n")