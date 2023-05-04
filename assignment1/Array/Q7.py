print("Write a function to insert an element at a specific position in the array")

n=int(input("Enter number of elements: "))
arr=[]
for i in range(0,n):
    ele=int(input("Enter elements:"))
    arr.append(ele)
print("Array is:",arr)
ele=int(input("Enter element to insert:"))
pos=int(input("Enter position to insert:"))
   
arr.insert(pos,ele)
print("Array after inserting element is:",arr)