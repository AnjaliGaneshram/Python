principle = int(input("Enter the principle amount: "))
rate = int(input("Enter the rate of interest: "))
time = int(input("Enter the time unit(in years): "))

Amount = principle * (1 + (rate/100))**time
C_I = Amount - principle
print("Compound Interest =", C_I)
