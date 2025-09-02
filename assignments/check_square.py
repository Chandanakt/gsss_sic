import math

num = int(input("Enter a number: "))
sqrt_num = math.sqrt(num)

if sqrt_num == int(sqrt_num):
    print(f"{num} is a perfect square.")
else:
    print(f"{num} is not a perfect square.")