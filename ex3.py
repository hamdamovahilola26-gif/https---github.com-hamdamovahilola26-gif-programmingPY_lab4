"""Exercise 3: repeatedly print n asterisks while n is positive."""

# Write your solution below.
while True:
    n = int(input("Enter n: "))
    if n > 0:
        print("*" * n)

    if n <= 0:
        print("Execution terminated.")
        break
    print()