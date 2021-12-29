import os
import sys

arg = sys.argv
assert len(arg) == 2
arg = arg[1]
path = "\\".join(os.path.realpath(__file__).split("\\")[:-1])

# Make folder named "0x"
if not os.path.exists(f"{path}\\{arg}"):
    os.mkdir(f"{path}\\{arg}")
# Make puzzle file, text files and python file
for file in ["sample.txt", "input.txt", "main.py", "puzzle.md"]:
    filePath = f"{path}\\{arg}\\{file}"
    if not os.path.exists(filePath):
        open(filePath, "w+").close()
with open(f"{path}\\{arg}\\main.py", "w") as file:
    file.write("import os\n\ndef read() -> str:\n\tpath = \"\\\\\".join(os.path.realpath(__file__).split(\"\\\\\")[:-1])\n\twith open(f\"{path}\\\\input.txt\", \"r\") as file:\n\t\treturn file.read().strip(\"\\n\")")
