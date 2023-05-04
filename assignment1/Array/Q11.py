print(" Write a program to find the common values between two arrays")

n1=int(input("Enter the size of array 1: "))
n2=int(input("Enter the size of array 2: "))
arr1=[]
arr2=[]
print("Enter the elements of array 1: ")
for i in range(n1):
    arr1.append(int(input()))
print("Enter the elements of array 2: ")
for i in range(n2):
    arr2.append(int(input()))
print("Common elements are: ")
for i in arr1:
    for j in arr2:
        if i==j:
            print(i,end=" ")
            break
print()