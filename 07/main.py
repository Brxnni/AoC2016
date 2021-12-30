import os
import re

def read() -> str:
	path = "\\".join(os.path.realpath(__file__).split("\\")[:-1])
	with open(f"{path}\\input.txt", "r") as file:
		return file.read().strip("\n")

def part1(file: str) -> int:

	def isAbba(string: str) -> bool:
		if len(string) > 4:
			# Check for every substring of length 4 when longer than 4 characters
			subStrings = [string[i:i + 4] for i in range(len(string) - 4)]
			return any([isAbba(subString) for subString in subStrings])		
		return string[0] == string[3] and string[1] == string[2]
    
	validCount = 0
	for ip in file.split("\n"):
		# Get everything inside square brackets
		hypernets = re.findall("\[.+?\]", ip)
		# Replace hypernets with delimiter
		for h in hypernets: ip = ip.replace(h, "|")
		# Get everything outside square brackets
		supernets = ip.split("|")
		# Remove square brackets from hypernets
		hypernets = [h[1:-1] for h in hypernets]
		# Check for abbas in hypernets, if theres any, not valid
		if any([isAbba(h) for h in hypernets]): continue
		# Check if theres any abba in supernets
		if any([isAbba(s) for s in supernets]): validCount += 1
	return validCount

def part2(file: str) -> int:
    
	def corresponding(aba: str, bab: str) -> bool:
		return aba[0] == aba[2] == bab[1] and aba[1] == bab[0] == bab[2]
    
	validCount = 0
	for ip in file.split("\n"):
		print(ip)
		# Get everything inside square brackets
		hypernets = re.findall("\[.+?\]", ip)
		# Replace hypernets with delimiter
		for h in hypernets: ip = ip.replace(h, "")
		# Get supernets as whole string
		supernets = ip
		# Remove square brackets from hypernets and join to one string
		hypernets = "".join([h[1:-1] for h in hypernets])
		# Get all possible ABAs from supernets
		abas = [supernets[i:i + 3] for i in range(len(supernets) - 2) if supernets[i] == supernets[i + 2] != supernets[i + 1]]
		if len(supernets) == 3: babs = [supernets]
		# Get all possible BABs from hypernets
		babs = [hypernets[i:i + 3] for i in range(len(hypernets) - 2) if hypernets[i] == hypernets[i + 2] != hypernets[i + 1]]
		if len(hypernets) == 3: babs = [hypernets]
		# Filter for BABs that fit to any ABA
		babs = [bab for bab in babs if any([corresponding(aba, bab) for aba in abas])]
		
		if len(babs) > 0: validCount += 1
	return validCount
