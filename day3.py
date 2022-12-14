def part1():
  file = open('./input/day3.txt')
  rucksacks = file.readlines()
  file.close()

  for rucksack in rucksacks:
    rucksackSize = len(rucksack)
    halfway = rucksackSize / 2
    first = rucksack[0, halfway]
    second = rucksack[half, len(rucksack)]