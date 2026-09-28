import sys

def is_nice(string):
  has_repeated_pair = False
  has_repeated_with_delim = False
  last_2 = '\0\0'
  for index, char in enumerate(string):
    last_2 = last_2[1] + char
    has_repeated_pair = has_repeated_pair or (last_2 in string[index+1:])
    #if index <= (len(string) - 3) and string[index+1] != string[index] and string[index+2] == string[index]:
    if index <= (len(string) - 3) and string[index+2] == string[index]:
      has_repeated_with_delim = True

  return has_repeated_pair and has_repeated_with_delim


total_nice = 0
for line in sys.stdin:
  if is_nice(line):
    total_nice += 1

print(total_nice)