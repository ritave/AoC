import sys
dial = 50
password = 0

for line in sys.stdin:
  direction = line[0]
  rotation = int(line[1:])
  if direction == 'L':
    rotation *= -1
  dial = (dial + rotation) % 100
  if dial == 0:
    password += 1
print(password)