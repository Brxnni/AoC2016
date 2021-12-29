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
	file2 = []
	for chunk in chunks:
		# Split chunk to lines
		chunk = [triangle.strip().replace("   ", " ").replace("  ", " ") for triangle in chunk]
		# Split to ints
		a1, b1, c1 = map(int, chunk[0].split(" "))
		a2, b2, c2 = map(int, chunk[1].split(" "))
		a3, b3, c3 = map(int, chunk[2].split(" "))
		# Add to file		
		file2.extend([f"{a1} {a2} {a3}", f"{b1} {b2} {b3}", f"{c1} {c2} {c3}"])
	# Just pass the data to part 1 :)
	return part1("\n".join(file2))
