import sys

elves = []

data = sys.stdin.readlines() + ['\n']
current_elf = 0
for line in data:
    if line == '\n':
      elves.append(current_elf)
      current_elf = 0
    else:
      current_elf += int(line)
elves.sort()
print(sum(elves[-3:]))