print("Write a function to find the duplicate values of an array of integer values")
n=int(input("Enter number of elements: "))
arr=[]
for i in range(0,n):
    ele=int(input("Enter elements:"))
    arr.append(ele)
print("Array is:",arr)
arr1=[]
for i in range(0,n):
    for j in range(i+1,n):
        if(arr[i]==arr[j]):
            arr1.append(arr[i])
print("Duplicate elements are:",arr1)
print("\n \n")