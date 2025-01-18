n = int(input("enter number of elements to be in tuple "))
print("enter elements to go in tuple")
tpl = ()
for i in range(0,n):
    tpl = list(tpl)
    tpl.append(input())
    tpl = tuple(tpl)
tpl2 = tpl[::-3]
tpl3 = tpl[2:9:2]
print("The tuple with every third element in reverse order:",tpl2)
print("The tuple with every alternate element between 3rd and 9th:",tpl3)