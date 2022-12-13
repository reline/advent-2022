def allCalories():
    file = open('./input/day1.txt')
    elves = file.readlines()
    file.close()

    calories = 0
    allCalories = []
    for elf in elves:
        if (elf.isspace()):
            allCalories.append(calories)
            calories = 0
        else:
            calories += int(elf)
    return allCalories

def part1():
    print(max(allCalories()))

def part2():
    calories = allCalories()
    calories.sort()
    print(calories[len(calories) - 1] + calories[len(calories) - 2] + calories[len(calories) - 3])

part1()
part2()