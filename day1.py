def part1():
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
    print(max(allCalories))

part1()