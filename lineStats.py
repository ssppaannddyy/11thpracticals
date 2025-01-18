aLine = input("Enter a String/Line: ")
uLtr = 0
lLtr = 0
alpha = 0
symbl = 0
digit = 0
for i in aLine:
    if i.isalpha():
        alpha = alpha + 1
        if i.isupper():
            uLtr = uLtr + 1
        elif i.islower():
            lLtr = lLtr + 1
    if i.isdigit():
        digit = digit + 1
    elif not i.isalnum():
        symbl = symbl + 1
print("Number of uppercase letters:",uLtr)
print("Number of alphabets:", alpha)
print("Number of symbols:", symbl)
print("Number of lowercase letters", lLtr)
print("Number of digits:",digit)