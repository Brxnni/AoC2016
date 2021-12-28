import os

def read() -> str:
	path = "\\".join(os.path.realpath(__file__).split("\\")[:-1])
	with open(f"{path}\\input.txt", "r") as file:
		return file.read()

def part1(file: str) -> int:
	# Parse instructions
	instructions = file.split(", ")
	# Interpret instructions
	position = [0, 0]
	direction = 0 # North = 0, East = 1, South = 2, West = 3
	for i in instructions:
		turn, amount = i[0], i[1:]
		amount = int(amount)
		# Turn left or right
		if turn == "L": direction = (direction - 1) % 4
		elif turn == "R": direction = (direction + 1) % 4
		# Add to either x or y value
		match direction:
			case 0: position[1] += amount
			case 1: position[0] += amount
			case 2: position[1] -= amount
			case 3: position[0] -= amount
	# Get distance from position to (0, 0)
	distance = abs(position[0]) + abs(position[1])
	return distance

# This is essentially part1, but with a list of visited locations and it breaks early when the location is already in the set
def part2(file: str) -> int:
	visited = [[0, 0]]
	# Parse instructions
	instructions = file.split(", ")
	# Interpret instructions
	position = [0, 0]
	direction = 0 # North = 0, East = 1, South = 2, West = 3
	for i in instructions:
		turn, amount = i[0], i[1:]
		amount = int(amount)
		# Turn left or right
		if turn == "L": direction = (direction - 1) % 4
		elif turn == "R": direction = (direction + 1) % 4
		isVisited = False
		# Add to either x or y value
		print(direction, amount)
		subPositions = []
		for _ in range(amount):
			match direction:
				case 0: position[1] += 1
				case 1: position[0] += 1
				case 2: position[1] -= 1
				case 3: position[0] -= 1
			if position in visited: isVisited = True; break
			# We need to "re-make" position because if we parse the variable,
			# we pass the reference and everything breaks.
			subPositions.append([*position])
		visited.extend(subPositions)
		if isVisited: break
	# Get distance from position to (0, 0)
	distance = abs(position[0]) + abs(position[1])
	return distance

print("> Answer:", part2(read()))
