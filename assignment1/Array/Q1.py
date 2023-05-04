print("Write a function to add integer values of an array")

n = int(input("Enter number of elements: "))
arr = []
for i in range(0,n):
    ele = int(input("Enter elements:"))
    arr.append(ele)
print("Array is:",arr)

def sum(arr):
    sum = 0
    for i in arr:
        sum = sum + i
    return sum
print("Sum of array elements is:",sum(arr))
print("\n \n")