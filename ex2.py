"""Exercise 2: print each requested figure for a positive integer n."""

# Write your solutions below.
#Первая программа
for i in range(4):
    stars = "*" * (4 - i)
    spaces =  "" * (2 * i+5)
    print(stars+spaces+stars)

    print()

#Вторая программа
    for i in range(4):
        if i == 0 or i == 3:
            print("****")
        else:
            print("* *")

        print()

#Третья программа
for i in range(4):
    dashes = "-" * i
    pluses = "+" * (3 - i)
    print(dashes + "*" + pluses)

print()

#Четвертая программа
for i in range(4):
    if i == 0 or i == 3:
        print("* *")
    else:
        print("**")   