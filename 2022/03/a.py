import sys

data = sys.stdin.readlines()

def priority(letter):
  o = ord(letter)
  if o >= ord('a') and o <= ord('z'):
    return o - ord('a') + 1
  else:
    return o - ord('A') + 27

result = 0
for rucksack in data:
  rucksack = rucksack[:-1]
  length = len(rucksack)
  fst, snd = rucksack[:length//2], rucksack[length//2:]
  s = set(fst).intersection(snd)
  assert len(s) == 1
  result += priority(s.pop())
print(result)
