def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def combinations(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

rows = int(input("Enter the number of rows for Pascal's triangle: "))
for i in range(rows):
    # Print leading spaces for alignment
    print(" " * (rows - i - 1), end="")
    for j in range(i + 1):
        print(combinations(i, j), end=" ")
    print()