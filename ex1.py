"""Exercise 1: display the two requested number series."""

# Write your solution below.
#Первая программа 
for i in range(10):

    for j in range(10):
         print(f"({i},{j})", end=" ")

         print()

#Вторая программа
for i in range(10):
    for j in range(10):
        num = 10 * i + j
        print(f"{num:<3}", end="")

        print()