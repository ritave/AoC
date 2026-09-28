import sys

total = 0

for line in sys.stdin:
  l, w, h = (int(dimension) for dimension in line.split('x'))
  volume = l * w * h
  a = 2*l + 2*w
  b = 2*w + 2*h
  c = 2*h + 2*l
  smallest = min(a, b, c)

  total += smallest + volume

print(total)