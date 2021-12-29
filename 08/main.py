import os

def read() -> str:
	path = "\\".join(os.path.realpath(__file__).split("\\")[:-1])
	with open(f"{path}\\input.txt", "r") as file:
		return file.read().strip("\n")

def renderDisplay(display: list[list[bool]]) -> None:
	print("-" * (len(display[0]) + 2))
	for row in display:
		print("|", end = "")
		for cell in row:
			print("#" if cell else " ", end = "")
		print("|")
	print("-" * (len(display[0]) + 2))

def part1(file: str) -> int:
    # Display is 2d array, every pixel is one boolean
	display = [[False for __ in range(50)] for _ in range(6)]

	for instruction in file.split("\n"):
		if instruction.startswith("rect"):
			# Split after the space at "x"
			instruction = instruction.split(" ")[1]
			width, height = map(int, instruction.split("x"))
			# Fill every row with a new sublist purely made of Trues
			for i in range(height):
				display[i][:width] = [True for _ in range(width)]
		elif instruction.startswith("rotate column"):
			instruction = instruction.split(" ")[2:]
			columnIndex = int(instruction[0][2:])
			amount = int(instruction[-1])
			# Extract column to list
			column = [display[i][columnIndex] for i in range(len(display))]
			# Shift column by amount
			amount = -amount % len(column)
			column = [*column[amount:], *column[:amount]]
			# Put column back
			for i, cell in enumerate(column):
				display[i][columnIndex] = cell
		elif instruction.startswith("rotate row"):
			instruction = instruction.split(" ")[2:]
			rowIndex = int(instruction[0][2:])
			amount = int(instruction[-1])
			# Extract row to list
			row = display[rowIndex]
			# Shift row by amount
			amount = -amount % len(display[0])
			row = [*row[amount:], *row[:amount]]
			# Put row back
			display[rowIndex] = row
		renderDisplay(display)

	print(sum([row.count(True) for row in display]))

# part2 doesnt exist because you need to read the output yourself
# and i am not writing a function to analyze this ascii mess and
# parse it to text. just no
