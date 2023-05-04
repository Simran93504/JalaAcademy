print("Write a function to find the minimum and maximum value of an array")

n=int(input("Enter number of elements: "))
arr=[]
for i in range(0,n):
    ele=int(input("Enter elements:"))
    arr.append(ele)
print("Array is:",arr)
print("Maximum value of array is:",max(arr))
print("Minimum value of array is:",min(arr))
print("\n \n")
