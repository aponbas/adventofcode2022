def get_value(item):
    v = ord(item)
    if item.islower():
        v -= 96
    else:
        v -= 38
    return v


def puzzle3():
    with open("input_3.txt", "r") as f:
        data = f.read().splitlines()

    score = 0
    for row in data:
        half = round(len(row) / 2)
        first_half = row[:half]
        second_half = row[half:]
        for item in first_half:
            if item in second_half:
                score += get_value(item)
                break

    print(f"Part 1 answer: {score}")

    score = 0
    for group_number in range(0, 100):
        group_start = group_number * 3
        first_elf = data[group_start]
        second_elf = data[group_start + 1]
        third_elf = data[group_start + 2]
        for item in first_elf:
            if item in second_elf and item in third_elf:
                score += get_value(item)
                break

    print(f"Part 2 answer: {score}")


if __name__ == "__main__":
    puzzle3()
