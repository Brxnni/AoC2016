import os
import sys
import hashlib

fullPath = "\\".join(os.path.realpath(__file__).split("\\")[:-2])
sys.path.append(fullPath)
import playsound

def part1(string: str) -> str:
	password = ""
	i = 0
	while True:
		# Hash and turn to hex
		hexHash = hashlib.md5((string + str(i)).encode()).hexdigest()
		if hexHash.startswith("00000"):
			# Add 6th character
			password += hexHash[5]
			# Return when done
			if len(password) == 8: return password
		i += 1

def part2(string: str) -> str:
	password = ["_" for _ in range(8)]
	i = 0
	while True:
		# Hash and turn to hex
		hexHash = hashlib.md5((string + str(i)).encode()).hexdigest()
		if hexHash.startswith("00000"):
			print(i, hexHash, "".join(password))
			# Char and position are first two non-zero hex digits
			char, position = hexHash[6], int(hexHash[5], 16)
			# Only set when position within range and char not already set
			if position < 8:
				if password[position] == "_":
					password[position] = char
					print("Set char", char, "at position", position, "pw is", "".join(password))
					# Play sound when one char is complete (my pc is slow sadge)
					playsound.play(f"{fullPath}\\done.mp3")
					if password.count("_") == 0: return "".join(password)
		i += 1

sample = "abc"
input = "ffykfhsq"
