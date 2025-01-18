marks = {}
for i in range (0,4):
    a = int(input("Enter roll number of student "))
    if a in marks.keys():
        print("that roll number is already present, please change it")
        i = i-1
        continue
    b = int(input("Enter marks of student "))
    marks.update({a:b})
print("Dictionary of students roll numbers and marks:",marks)