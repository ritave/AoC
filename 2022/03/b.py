import sys

data = sys.stdin.readlines()
assert len(data) % 3 == 0

def group(count, arr):
  return (arr[i:i+count] for i in range(0, len(arr), count))

def priority(letter):
  o = ord(letter)
  if o >= ord('a') and o <= ord('z'):
    return o - ord('a') + 1
  else:
    return o - ord('A') + 27

result = 0
for (a, b, c) in group(3, data):
  a = a[:-1]
  b = b[:-1]
  c = c[:-1]
  s = set(a).intersection(b).intersection(c)
  assert len(s) == 1
  result += priority(s.pop())
print(result)
