
"""Exercise 4: print Floyd's triangle by rows and by number count."""

# Part 1
n = int(input("n for rows: "))
number = 1

for row in range(1, n + 1):
	for column in range(row):
		print(number, end=" ")
		number = number + 1
	print()

# Part 2
n = int(input("n for numbers: "))
number = 1
row = 1

while number <= n:
	column = 0
	while column < row and number <= n:
		print(number, end=" ")
		number = number + 1
		column = column + 1
	print()
	row = row + 1
