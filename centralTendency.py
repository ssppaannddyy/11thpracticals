import random,statistics
ll = int(input("Enter the lower limit of numbers to be generated: "))
ul = int(input("Enter the upper limit of numbers to be generated: "))
s = int(input("Enter if the numbers should be a multiple of this number (else put 1): "))
l1 = []
for i in range(0,6):
    val = random.randrange(ll,ul,s)
    l1.append(val)
print("Randomly generated values: ",l1)
mean = statistics.mean(l1)
median = statistics.median(l1)
mode = statistics.mode(l1)
print("Mean of the values =",mean)
print("Median of the values =",median)
print("Mode of the values =",mode)