print("Write a function to remove a specific element from an array")

n=int(input("Enter number of elements: "))
arr=[]
for i in range(0,n):
    ele=int(input("Enter elements:"))
    arr.append(ele)
print("Array is:",arr)
ele=int(input("Enter element to remove:"))
for i in range(0,n):
    if(arr[i]==ele):
        arr.remove(ele)
        print("Element removed")
        break
    else:
        print("Element not found")
        break
print("Array after removing element is:",arr)
