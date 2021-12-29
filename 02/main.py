import os
import math
from types import coroutine

def read() -> str:
	path = "\\".join(os.path.realpath(__file__).split("\\")[:-1])
	with open(f"{path}\\input.txt", "r") as file:
		return file.read()

def part1(file: str) -> str:
	keypad = [1,2,3,4,5,6,7,8,9]
	currentButton = 5
	buttons = ""

	for line in file.split("\n"):
		# Get 2d coordinate of where the current button
		coordinate = [(currentButton - 1) % 3, currentButton // 3 - 1]
		# Change coordinate for every character, but dont move when hitting edge
		for direction in line:
			match direction:
				case "U":
					if coordinate[1] > 0: coordinate[1] -= 1
				case "R":
					if coordinate[0] < 2: coordinate[0] += 1
				case "D":
					if coordinate[1] < 2: coordinate[1] += 1
				case "L":
					if coordinate[0] > 0: coordinate[0] -= 1
		# This set of instructions is done, write down button
		currentButton = keypad[3 * coordinate[1] + coordinate[0]]
		buttons += str(keypad[3 * coordinate[1] + coordinate[0]])

	return buttons

def part2(file: str) -> str:
	keypad = [
		["0","0","1","0","0"],
		["0","2","3","4","0"],
		["5","6","7","8","9"],
		["0","A","B","C","0"],
		["0","0","D","0","0"]
	]
	buttons = ""
	# Coordinate system's (0, 0) is top left
	coordinate = [0, 2]
	for line in file.split("\n"):
		# Loop through every direction
		for direction in line:
			match direction:
				case "U":
					# Normally you would put both inside one if statement,
					# but we need to check them in order to not crash
					# Check if we are not on the total edge
					if coordinate[1] > 0:
						# Check if we would move to a "0"
						if keypad[coordinate[1] - 1][coordinate[0]] != "0": coordinate[1] -= 1
				case "R":
					if coordinate[0] < 4:
						if keypad[coordinate[1]][coordinate[0] + 1] != "0": coordinate[0] += 1
				case "D":
					if coordinate[1] < 4:
						if keypad[coordinate[1] + 1][coordinate[0]] != "0": coordinate[1] += 1
				case "L":
					if coordinate[0] > 0:
						if keypad[coordinate[1]][coordinate[0] - 1] != "0": coordinate[0] -= 1
		buttons += keypad[coordinate[1]][coordinate[0]]
	return buttons
