class Tail:
    def __init__(self, i, j):
        self.i = i
        self.j = j

class Head:
def puzzle9():
    with open("input_9.txt", "r") as f:
        data = f.read().splitlines()

    total_size = 500
    grid_length = grid_width = total_size
    grid = []
    for i in range(0, grid_width):
        grid.append([" "] * grid_length)

    tail_grid = []
    for i in range(0, grid_width):
        tail_grid.append([" "] * grid_length)

    i = int(total_size/2)
    j = int(total_size/2)
    tail_grid[i][j] = "T"
    tail = Tail(i, j)
    for line in data:
        direction = line[0]
        space = int(line[2:])
        for move in range(space):
            if direction == "U":
                i -= 1
            elif direction == "D":
                i += 1
            elif direction == "L":
                j -= 1
            elif direction == "R":
                j += 1
            grid[i][j] = "H"
            print(f"H: {i}, {j}. T: {tail.i}, {tail.j}")
            if abs(tail.i-i) + abs(tail.j-j) > 2:
                if (i - tail.i) < 0 and (j - tail.j) < 0:
                    tail.i -= 1
                    tail.j -= 1
                    # i-1, j-1
                if (i - tail.i) > 0 and (j - tail.j) > 0:
                    tail.i += 1
                    tail.j += 1
                    # i+1, j+1
                if (i - tail.i) < 0 and (j - tail.j) > 0:
                    tail.i -= 1
                    tail.j += 1
                    # i-1, j+1
                if (i - tail.i) > 0 and (j - tail.j) < 0:
                    tail.i += 1
                    tail.j -= 1
                    # i+1, j-1
                # diagonal move
            elif abs(tail.i-i) > 1:
                if i-tail.i > 0:
                    tail.i += 1
                else:
                    tail.i -= 1
            elif abs(tail.j-j) > 1:
                print(direction)
                if j-tail.j > 0:
                    tail.j += 1
                else:
                    tail.j -= 1
            print(f"{direction}, {move}")
            print(f"H: {i}, {j}. T: {tail.i}, {tail.j}")
            tail_grid[tail.i][tail.j] = "T"

    for line in grid:
        print(line)
    print("---")
    for line in tail_grid:
        print(line)

    total = 0
    for line in tail_grid:
        for x in line:
            if x == "T":
                total += 1

    print(total)
    # print(f"Part 1 answer: {visible_trees}")
    # print(f"Part 2 answer: {max_scenic_score}")


if __name__ == "__main__":
    puzzle9()
