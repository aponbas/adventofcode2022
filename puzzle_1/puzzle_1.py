def puzzle1():
    with open("input_1.txt", "r") as f:
        data = f.readlines()

    calories = []
    total_calories = 0
    for row in data:
        if row == "\n":
            calories.append(total_calories)
            total_calories = 0
            continue
        total_calories += int(row)

    calories.sort()

    print(f"Part 1 answer: {calories[-1:][0]}")
    print(f"Part 2 answer: {sum(calories[-3:])}")


if __name__ == "__main__":
    puzzle1()
