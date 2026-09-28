import sys

data = sys.stdin.readlines()

empty_index = data.index('\n')

stacks_data = data[:empty_index-1]
moves_data = data[:empty_index+1:]

stacks = []
for (index, char) in enumerate(stacks_data[-1][:-1]):
  if char != ' ':
    stacks.append([])


moves = []
for move in moves_data:
  move = move.split(' ')
  moves.append((int(move[1]), int(move[3]), int(move[5])))