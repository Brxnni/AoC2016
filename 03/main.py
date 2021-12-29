import os

def read() -> str:
	path = "\\".join(os.path.realpath(__file__).split("\\")[:-1])
	with open(f"{path}\\input.txt", "r") as file:
		return file.read()

def part1(file: str) -> str:
	possible = 0
	for triangle in file.split("\n"):
		# Get rid of extra spaces
		triangle = triangle.strip().replace("   ", " ").replace("  ", " ")
		# Parse to integers
		a, b, c = triangle.split(" ")
		a, b, c = map(int, (a, b, c))
		# Check all 3 combinations
		if (
			a + b > c and
			b + c > a and
			a + c > b
		): possible += 1;
	return possible

def part2(file: str) -> str:
	# Restructure file to use rows again
	# Split to three-line blocks
	lines = file.split("\n")
	chunks = [lines[i:i + 3] for i in range(0, len(lines), 3)]
	### TODO: Loop through all the chunks and mirror them on the diagonal so its like 3 rows instead of 3 columns

print(part1(read()))