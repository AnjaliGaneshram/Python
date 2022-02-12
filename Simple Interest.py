pri = float(input("Enter the principal amount: "))
time = int(input("Enter the time(in years): "))
rate = int(input("Enter the rate of interest: "))

S_I = float(((pri * time * rate)/100))

print("Simple Interest =", S_I)
