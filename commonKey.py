D1 = {}
D2 = {}
n1 = int(input("Enter number of elements to be in first dictionary"))
for i in range (0,n1):
    a = input("Enter key: ")
    if a in D1.keys():
        print("please try again, as the key already exists")
        i=i-1
        continue
    b = input("Enter value corresponding to the key: ")
    D1.update({a:b})
n2 = int(input("Enter number of elements to be in second dictionary"))
for i in range (0,n2):
    a = input("Enter key: ")
    if a in D2.keys():
        print("please try again, as the key already exists")
        i=i-1
        continue
    b = input("Enter value corresponding to the key: ")
    D2.update({a:b})
l1 = D1.keys()
l2 = D2.keys()
lc = []
for i in l1:
    if i in l2:
        lc.append(i)
print("List of common keys:",lc)