import sys
dial = 50
password = 0

for line in sys.stdin:
  direction = line[0]
  rotation = int(line[1:])

  #print('===')
  #print('dial', dial)
  #print('rotation', direction, rotation)
  for i in range(rotation):
    if direction == 'L':
      dial -= 1
    else:
      dial += 1

    dial %= 100
    #print('\tdial', dial)


    if (dial == 0):
      password += 1
      #print('\tpassword', password)
  #print('\tstopped at:', dial)

print(password)