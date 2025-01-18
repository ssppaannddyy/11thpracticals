eng = float(input("enter marks obtained in english "))
phy = float(input("enter marks obtained in physics "))
che = float(input("enter marks obtained in chemistry "))
mth = float(input("enter marks obtained in maths "))
csc = float(input("enter marks obtained in computer science "))

total = (eng+phy+che+mth+csc)
avg = total/(5*100)
pct = avg * 100

fl = False
if eng > 100 or phy > 100 or che > 100 or mth > 100 or csc > 100:
    fl = True

print()
print("max marks: ",(5*100))
print("marks obtained: ",total)
print("percentage of marks: ",pct)

if pct > 100 or fl:
    print("maybe there's some error somewhere...?")