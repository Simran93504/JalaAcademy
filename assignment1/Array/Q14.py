print("Write a method to find number of even number and odd numbers in an array")
n=int(input("Enter the size of array: "))
arr=[]
print("Enter the elements of array: ")
for i in range(n):
    arr.append(int(input()))
even=0
odd=0
for i in arr:
    if i%2==0:
        even+=1
    else:
        odd+=1
print("Number of even numbers: ",even)
print("Number of odd numbers: ",odd)