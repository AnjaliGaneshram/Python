mark = int(input("Enter your mark: "))
if mark>100 or mark<0:
    print("Invalid mark")
elif mark<50:
    print("Fail")
elif mark>50:
    print("Pass")
    if mark >=50 and mark <60:
        print("Grade: E")
    elif mark>=60 and mark < 70:
        print("Grade: D")
    elif mark>=70 and mark<80:
        print("Grade: C")
    elif mark>=80 and mark<90:
        print("Grade: B")
    elif mark>=90 and mark<=100:
        print("Grade: A")
