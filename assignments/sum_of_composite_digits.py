n = int(input("Enter a number: "))
s = str(n)
composite_digits = {4, 6, 8, 9}
total = 0

for digit_char in s:
    digit = int(digit_char)
    if digit in composite_digits:
        total += digit

print(f"The sum of composite digits is: {total}")