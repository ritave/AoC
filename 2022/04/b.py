import sys

def overlaps(a, b):
  left = max(a[0], b[0])
  right = min(a[1], b[1])
  return right - left >= 0

total_contained = 0

data = sys.stdin.readlines()
for pair in data:
  left, right = pair.split(',')
  left = [int(x) for x in left.split('-')]
  right = [int(x) for x in right.split('-')]
  if overlaps(left, right):
    total_contained += 1
print(total_contained)