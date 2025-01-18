n = int(input("Enter how many people are present in the class "))
print("Enter",n,"Student names:")
names = []
for i in range(0,n):
    names = list(names)
    names.append(input())
    names = tuple(names)
name = input("Enter name of student to search: ")
if name in names:
    print("Yes, the name",name,"is present in this tuple")
else:
    print("No, the name is not present in the tuple")