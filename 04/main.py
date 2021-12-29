import os

def read() -> str:
	path = "\\".join(os.path.realpath(__file__).split("\\")[:-1])
	with open(f"{path}\\input.txt", "r") as file:
		return file.read().strip("\n")

def part1(file: str) -> int:
    sectorSum = 0
    for room in file.split("\n"):
        # Parse line
        roomName = room[:room.rindex("-")]
        sectorID = int(room[room.rindex("-") + 1:room.index("[")])
        checksum = room[room.index("[") + 1:-1]
        # List amount of letters
        letters = [[letter, roomName.count(letter)] for letter in "abcdefghijklmnopqrstuvwxyz" if roomName.count(letter) > 0]
        letters.sort(key = lambda l: -l[1])
        correctChecksum = "".join(l[0] for l in letters[:5])
        # Compare
        if checksum == correctChecksum:
            sectorSum += sectorID
    return sectorSum

def part2(file: str) -> int:
	# This is fucking stupid, I didn't understand what the last line ment and
	# I had to *google* the correct string to look for. wtf bro just tell me the string
	solution = "north"
	letters = "abcdefghijklmnopqrstuvwxyz"
	for room in file.split("\n"):
		# Get name
		roomName = room[:room.rindex("-")]
		sectorID = int(room[room.rindex("-") + 1:room.index("[")])
		# Shift name
		newRoomName = ""
		for letter in roomName:
			if letter != "-":
				newRoomName += letters[(letters.index(letter) + sectorID) % 26]
			else:
				newRoomName += " "
		if solution in newRoomName:
			print(roomName, newRoomName, sectorID)
			return sectorID
