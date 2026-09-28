
possible_moves = {
  '>': ( 1,  0),
  'v': ( 0,  1),
  '<': (-1,  0),
  '^': ( 0, -1)
}

directions = input()

at = (0, 0)
visited = set([at])
for movement in directions:
  x,y = possible_moves[movement]
  at = (at[0] + x, at[1] + y)
  visited.add(at)
print(len(visited))
