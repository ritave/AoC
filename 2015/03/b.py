
possible_moves = {
  '>': ( 1,  0),
  'v': ( 0,  1),
  '<': (-1,  0),
  '^': ( 0, -1)
}

directions = input()

santa_at = (0, 0)
robot_at = (0, 0)
visited = set([(0, 0)])
santa_is_moving = False

for movement in directions:
  x,y = possible_moves[movement]

  if santa_is_moving:
    santa_at = (santa_at[0] + x, santa_at[1] + y)
    visited.add(santa_at)
  else:
    robot_at = (robot_at[0] + x, robot_at[1] + y)
    visited.add(robot_at)
  santa_is_moving = not santa_is_moving

print(len(visited))
