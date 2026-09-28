import sys

total = 0

for line in sys.stdin:
  l, w, h = (int(dimension) for dimension in line.split('x'))
  a = l*w
  b = w*h
  c = h*l
  smallest = min(a, b, c)
  total += 2*a + 2*b + 2*c + smallest

print(total)