print("Write a function to reverse an array of integer values")

n=int(input("Enter number of elements: "))
arr=[]
for i in range(0,n):
    ele=int(input("Enter elements:"))
    arr.append(ele)
print("Array is:",arr)
arr.reverse()
print("Reversed array is:",arr)
print("\n \n")
