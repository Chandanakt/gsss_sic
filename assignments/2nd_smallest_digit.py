n = int(input("Enter a number: "))
digits = sorted(list(set(str(n))))
if len(digits) >= 2:
    print(f"The 2nd smallest digit is: {digits[1]}")
else:
    print("Not enough unique digits to find the 2nd smallest.")