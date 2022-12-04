def puzzle4():
    with open("input_4.txt", "r") as f:
        data = f.read().splitlines()

    score_part_1 = 0
    score_part_2 = 0
    for row in data:
        s = row.split(",")

        set_one_split = s[0].split("-")
        set_two_split = s[1].split("-")

        set_one_start = int(set_one_split[0])
        set_one_end = int(set_one_split[1])
        set_two_start = int(set_two_split[0])
        set_two_end = int(set_two_split[1])

        set_one = set(range(set_one_start, set_one_end+1))
        set_two = set(range(set_two_start, set_two_end+1))

        if set_one.issubset(set_two) or set_two.issubset(set_one):
            score_part_1 += 1
        if set_one.intersection(set_two):
            score_part_2 += 1

    print(f"Part 1 answer: {score_part_1}")
    print(f"Part 2 answer: {score_part_2}")


if __name__ == "__main__":
    puzzle4()
