challenge = input()
floor = 0

for char in challenge:
  if char == '(':
    floor += 1
  elif char == ')':
    floor -= 1
  else:
    raise ValueError()

print(floor)