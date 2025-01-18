x,y,z = int(input("enter how many days x can get work done in: ")), int(input("enter how many days y can get work done in: ")), int(input("enter how many days z can get work done in: "))
d = x*y*z/(x*y + y*z + x*z)
print("they can get the work done together in ",d,"days")