import sys

enemy_map = { "A": 'rock', "B": 'paper', "C":'scissors' }
player_map = { "X": 'rock', "Y": 'paper', "Z": 'scissors' }
score_map = {'rock': 1, 'paper': 2, 'scissors': 3}

def score_round(enemy, player):
  enemy_score = score_map[enemy]
  player_score = score_map[player]
  if enemy == 'rock':
    if player == 'rock':
      enemy_score += 3
      player_score += 3
    elif player == 'paper':
      enemy_score += 0
      player_score += 6
    else:
      enemy_score += 6
      player_score += 0
  elif enemy == 'paper':
    if player == 'rock':
      enemy_score += 6
      player_score += 0
    elif player == 'paper':
      enemy_score += 3
      player_score += 3
    else:
      enemy_score += 0
      player_score += 6
  else:
    if player == 'rock':
      enemy_score += 0
      player_score += 6
    elif player == 'paper':
      enemy_score += 6
      player_score += 0
    else:
      enemy_score += 3
      player_score += 3
  return [enemy_score, player_score]

player_score = 0

data = sys.stdin.readlines()
for line in data:
  enemy, player = line[:-1].split(' ')
  enemy = enemy_map[enemy]
  player = player_map[player]
  player_score += score_round(enemy, player)[1]
print(player_score)