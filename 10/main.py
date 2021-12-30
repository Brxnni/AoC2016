import os

def read() -> str:
	path = "\\".join(os.path.realpath(__file__).split("\\")[:-1])
	with open(f"{path}\\input.txt", "r") as file:
		return file.read().strip("\n")

# This function solves both parts.
def part12(file: str) -> int:
	# Parse input values
	bots = {}
	for line in [l for l in file.split("\n") if l.startswith("value")]:
		chipNum = line.split(" ")[1]
		botNum = line.split(" ")[-1]
		if botNum in bots: bots[botNum].append(int(chipNum))
		else: bots[botNum] = [int(chipNum)]
		file = file.replace(line + "\n", "")
	# This is what we are looking for	
	compare =  [61, 17]
	compare.sort()
	# Repeat procedure until right bot number has been found
	# (comparing 61 and 17)
	outputs = {}
	comparer = -1
	while any(bots.values()):
		for line in [l for l in file.split("\n") if not l.startswith("value")]:
			line = line.split(" ")
			# Parse line
			botNum = line[1]
			lower = line[6]
			higher = line[-1]
			# Bools whether to throw value away or give to bot num
			lowerOutput = line[5] == "output"
			higherOutput = line[-2] == "output"
			if not botNum in bots: continue
			if len(bots[botNum]) == 2:
				# Check if responsible for our goal, if so
				# save number and return at the very end
				array = [min(bots[botNum]), max(bots[botNum])]
				if array == compare: comparer = botNum
				# Otherwise, continue on normal execution	
				# Append higher/lower value to bots
				if not lowerOutput:
					if lower in bots: bots[lower].append(min(bots[botNum]))
					else: bots[lower] = [min(bots[botNum])]
				else: outputs[lower] = min(bots[botNum])
				if not higherOutput:
					if higher in bots: bots[higher].append(max(bots[botNum]))
					else: bots[higher] = [max(bots[botNum])]
				else: outputs[higher] = max(bots[botNum])
				# Remove value from original bot
				bots[botNum] = []
	return comparer, outputs["0"] * outputs["1"] * outputs["2"]
