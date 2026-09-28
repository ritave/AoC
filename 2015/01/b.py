challenge = input()
floor = 0

for index, char in enumerate(challenge):
  if char == '(':
    floor += 1
  elif char == ')':
    floor -= 1
    if floor == -1:
      print(index + 1)
      break
  else:
    raise ValueError()