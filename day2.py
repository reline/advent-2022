bonuses = {'X': 1, 'Y': 2, 'Z': 3}
rps = {'A': 'X', 'B': 'Y', 'C': 'Z'}

def score(opponent, self):
  score = bonuses[self]
  if rps[opponent] == self:
    return score + 3
  if (opponent == 'A' and self == 'Y') or (opponent == 'B' and self == 'Z') or (opponent == 'C' and self == 'X'):
    return score + 6
  return score

def part1():
  file = open('./input/day2.txt')
  rounds = file.readlines()
  file.close()

  total_score = 0
  for round in rounds:
    plays = round.split(' ')
    total_score += score(plays[0], plays[1].strip())

  print(total_score)

part1()