n1 = int(input("Enter number of elements to be in first dictionary: "))
dict1 = {}
dict2 = {}
print("Enter elements for the first dictionary")
for i in range (0,n1):
    while True:
        a = input("Enter key: ")
        if a in dict1.keys():
            print("please try again, as the key already exists")
            continue
        b = input("Enter value corresponding to the key: ")
        dict1.update({a:b})
        break
n2 = int(input("Enter number of elements to be in second dictionary: "))
for i in range (0,n2):
    while True:
        c = input("Enter key: ")
        if c in dict2.keys():
            print("please try again, as the key already exists")
            continue
        d = input("Enter value corresponding to key: ")
        dict2.update({c:d})
        break
mDict = dict1.copy()
for i in dict2.keys():
     if i not in dict1.keys():
         mDict[i] = dict2.get(i)
     else:
         a,b = dict1.get(i), dict2.get(i)
         if a>=b:
             mDict[i] = a
         else:
             mDict[i] = b
print("The merged Dictionary will be:",mDict)