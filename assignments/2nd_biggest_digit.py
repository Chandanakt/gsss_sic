n = int(input("Enter a number: "))
digits = sorted(list(set(str(n))), reverse=True)
if len(digits) >= 2:
    print(f"The 2nd biggest digit is: {digits[1]}")
else:
    print("2nd biggest digit cannot be found. The number has fewer than two unique digits.")