import sys

def is_nice(string):
  vowels = 'aeiou'
  total_vowels = 0
  has_repeated_letter = False
  cant_contain = set(['ab', 'cd', 'pq','xy'])
  last_2 = '\0\0'
  for char in string:
    if char in vowels:
      total_vowels += 1

    last_2 = last_2[1] + char
    if last_2[0] == last_2[1]:
      has_repeated_letter = True

    if last_2 in cant_contain:
      return False

  return has_repeated_letter and total_vowels >= 3


total_nice = 0
for line in sys.stdin:
  if is_nice(line):
    total_nice += 1

print(total_nice)