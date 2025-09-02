n = int(input("Enter a number: "))
s = str(n)
total = 0
for i in range(len(s)):
    if i % 2 == 0:
        total += int(s[i])
print(f"The sum of even-placed digits is: {total}")