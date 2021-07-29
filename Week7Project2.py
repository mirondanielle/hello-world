filename = input("Please enter file name: ")
lines = []
with open(filename, 'r') as fn:
    for line in fn:
        lines.append(line.strip())

while True:
    print("This file has", len(lines), "lines.")
    if len(lines) == 0:
        break
    lineNum = int(input("Enter a line number or enter 0 to quit: "))
    if lineNum == 0:
        break
    elif lineNum > len(lines):
        print("Error: The line number must be less than or equal to", len(lines))
    else:
        print(lineNum, ": ", lines[lineNum - 1])
