address = input("Enter the address: ")
adlist = address.split(" ")
pincode = 0
for i in adlist:
    if i.isdigit() and len(i)==6:
        pincode = i
print("Pincode:",pincode)