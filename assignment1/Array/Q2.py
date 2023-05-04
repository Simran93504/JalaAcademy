print("Write a function to calculate the average value of an array of integers")

n = int(input("Enter number of elements: "))
arr = []
for i in range(0,n):
    ele = int(input("Enter elements:"))
    arr.append(ele)
print("Array is:",arr)

def avg(arr):
    sum = 0
    for i in arr:
        sum = sum + i
    return sum/n
print("Average of array elements is:",avg(arr))