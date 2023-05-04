print("Write a program to find the index of an array element")

n = int(input("Enter number of elements: "))
arr = []
for i in range(0,n):
    ele = int(input("Enter elements:"))
    arr.append(ele)

print("Array is:",arr)
ele = int(input("Enter element to find index:"))
for i in range(0,n):
    if(arr[i]==ele):
        print("Index of element is:",i)
        break
    else:
        print("Element not found")
        break
print("\n \n")