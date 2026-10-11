"""Exercise 2: print each requested figure for a positive integer n."""

# Write your solutions below.
#Первая программа
n = int(input("Enter n: "))
for i in range(n):
    stars = "*" * (n - i)
    spaces =  " " * (2 * i+5)
    print(stars+spaces+stars)

    print()

#Вторая программа
for i in range(n):
    if i == 0 or i == n - 1:
        print("* " * n)
    else:
        print("* " + "  " * (n - 2) + "* ")
        
        
#Третья программа
for i in range(n):
    dashes = "-" * i
    pluses = "+" * (n - 1 - i)
    print(dashes + "*" + pluses)

print()

#Четвертая программа
for i in range(n):
    if i == 0 or i == n - 1:
        print(" *  * ")
    else:
        print("  **  ")   