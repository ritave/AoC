import sys

def contains(a, b):
  return a[0] <= b[0] and a[1] >= b[1]

total_contained = 0

data = sys.stdin.readlines()
for pair in data:
  left, right = pair.split(',')
  left = [int(x) for x in left.split('-')]
  right = [int(x) for x in right.split('-')]
  if contains(left, right) or contains(right, left):
    total_contained += 1
print(total_contained)