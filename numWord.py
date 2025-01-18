nDict = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}
n = int(input("Enter a number "))
sn = str(n)
snl = list(sn)
numWord = ""
for i in snl:
    i = int(i)
    numWord = numWord + str(nDict.get(i)) + " "
numWord = numWord.capitalize().strip()
print("The number", n, "in words is", numWord)
