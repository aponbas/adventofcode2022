def calculate_score(data, mapping):
    score = 0
    for game in data:
        score += mapping[game]
    return score


def puzzle1():
    with open("input_2.txt", "r") as f:
        data = f.read().split("\n")

    point_map_1 = {
        'A X': 4,
        'A Y': 8,
        'A Z': 3,
        'B X': 1,
        'B Y': 5,
        'B Z': 9,
        'C X': 7,
        'C Y': 2,
        'C Z': 6
    }

    score = calculate_score(data, point_map_1)
    print(f"Part 1 answer: {score}")

    point_map_2 = {
        'A X': 3,
        'A Y': 4,
        'A Z': 8,
        'B X': 1,
        'B Y': 5,
        'B Z': 9,
        'C X': 2,
        'C Y': 6,
        'C Z': 7
    }

    score = calculate_score(data, point_map_2)
    print(f"Part 2 answer: {score}")


if __name__ == "__main__":
    puzzle1()
