import os

def read() -> str:
	path = "\\".join(os.path.realpath(__file__).split("\\")[:-1])
	with open(f"{path}\\input.txt", "r") as file:
		return file.read().strip("\n")

def part1(file: str) -> int:
	if "(" not in file: return len(file)
	length = 0
	while "(" in file:
		length += file.find("(")
		file = file[file.find("("):]
		# Get amount of chars to be copied and amount of times
		charAmount, times = file[1:file.find(")")].split("x")
		file = file[file.find(")") + 1:]
		# Add charAmount * times to length
		length += int(charAmount) * int(times)
		file = file[int(charAmount):]
	length += len(file)
	return length

# This is the same as part 1, except it recursively
# solves everything before it gets it length

def part2(file: str) -> int:
	if "(" not in file: return len(file)
	length = 0
	while "(" in file:
		length += file.find("(")
		file = file[file.find("("):]
		# Get amount of chars to be copied and amount of times
		charAmount, times = file[1:file.find(")")].split("x")
		file = file[file.find(")") + 1:]
		# Add charAmount * times to length
		length += part2(file[:int(charAmount)]) * int(times)
		file = file[int(charAmount):]
	length += len(file)
	return length
