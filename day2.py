def part1(rounds):
  bonuses = {'X': 1, 'Y': 2, 'Z': 3}
  rps = {'A': 'X', 'B': 'Y', 'C': 'Z'}

  def score(opponent, self):
    score = bonuses[self]
    if rps[opponent] == self:
      return score + 3
    if (opponent == 'A' and self == 'Y') or (opponent == 'B' and self == 'Z') or (opponent == 'C' and self == 'X'):
      return score + 6
    return score

  total_score = 0
  for round in rounds:
    plays = round.split(' ')
    total_score += score(plays[0], plays[1].strip())

  print(total_score)

def part2(rounds):
  result_bonuses = {'X': 0, 'Y': 3, 'Z': 6}
  shape_bonuses = {'A': 1, 'B': 2, 'C': 3}

  bonuses = {
    'A': {
      'X': 'C',
      'Y': 'A',
      'Z': 'B',
    },
    'B': {
      'X': 'A',
      'Y': 'B',
      'Z': 'C',
    },
    'C': {
      'X': 'B',
      'Y': 'C',
      'Z': 'A',
    },
  }

  def score(opponent, result):
    return result_bonuses[result] + shape_bonuses[bonuses[opponent][result]]

  total_score = 0
  for round in rounds:
    plays = round.split(' ')
    total_score += score(plays[0], plays[1].strip())
  print(total_score)

file = open('./input/day2.txt')
rounds = file.readlines()
file.close()

part1(rounds)
part2(rounds)
