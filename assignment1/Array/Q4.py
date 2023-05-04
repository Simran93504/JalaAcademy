print("Write a function to test if array contains a specific value")

n = int(input("Enter number of elements: "))
arr = []
for i in range(0,n):
    ele = int(input("Enter elements:"))
    arr.append(ele)
print("Array is:",arr)
ele = int(input("Enter element to find:"))
for i in range(0,n):
    if(arr[i]==ele):
        print("Element found")
        break
    else:
        print("Element not found")
        break
    
print("\n \n")