import os

def read() -> str:
	path = "\\".join(os.path.realpath(__file__).split("\\")[:-1])
	with open(f"{path}\\input.txt", "r") as file:
		return file.read().strip("\n")

def part1(file: str) -> str:
	transmissions = file.split("\n")
	length = len(transmissions[0])
	message = ""
	for i in range(length):
		allChars = "".join([transmission[i] for transmission in transmissions])
		charCounts = [[char, allChars.count(char)] for char in set(allChars)]
		charCounts.sort(key = lambda c: c[1])
		charCounts.reverse()
		mostCommonChar = charCounts[0][0]
		message += mostCommonChar
	return message

# This is just part 1 but checking for the least common char (i.e. not reversing the charCounts list)
def part2(file: str) -> str:
	transmissions = file.split("\n")
	length = len(transmissions[0])
	message = ""
	for i in range(length):
		allChars = "".join([transmission[i] for transmission in transmissions])
		charCounts = [[char, allChars.count(char)] for char in set(allChars)]
		charCounts.sort(key = lambda c: c[1])
		mostCommonChar = charCounts[0][0]
		message += mostCommonChar
	return message

print(part2(read()))